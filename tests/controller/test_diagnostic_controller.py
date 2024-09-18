import pytest
from PySide6.QtCore import QCoreApplication
from src.model.diagnostic_model import DiagnosticModel
from src.controller.diagnostic_controller import DiagnosticController


@pytest.fixture
def diagnostic_model():
    """Fixture to initialize and clean up DiagnosticModel."""
    model = DiagnosticModel(udp_port=5001)
    yield model
    model.stop()


@pytest.fixture
def diagnostic_controller(diagnostic_model):
    """Fixture to initialize DiagnosticController."""
    controller = DiagnosticController(diagnostic_model)
    return controller


@pytest.fixture
def mock_udp_socket(monkeypatch):
    """Fixture to mock the UDP socket with a configurable message."""

    def _mock_udp_socket(message: bytes):
        """Configure the mock socket with the provided message."""

        def mock_recvfrom(*args, **kwargs):
            return (message, ('localhost', 5001))

        monkeypatch.setattr('socket.socket.recvfrom', mock_recvfrom)

    return _mock_udp_socket


def test_signal_emission(qtbot, diagnostic_controller, mock_udp_socket):
    # Define the test message for the left camera
    test_message = b'cam-left,50.0,30.0'
    mock_udp_socket(test_message)

    # Wait for the left camera signal
    with qtbot.waitSignal(diagnostic_controller.data_updated, timeout=100) as spy:
        diagnostic_controller.model._process_udp_data(test_message)

    # Ensure the signal was emitted correctly
    assert spy.signal_triggered, "Left camera signal was not emitted."
    assert spy.args == ["cam-left", 50.0, 30.0]

    # Verify data for the left camera
    assert diagnostic_controller.model.get_health_data('cam-left') == {
        'core_temp': 50.0,
        'cpu_usage': 30.0,
    }
