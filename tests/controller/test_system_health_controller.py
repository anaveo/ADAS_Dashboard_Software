import pytest
from PySide6.QtCore import QCoreApplication
from src.model.system_health_model import SystemHealthModel
from src.controller.system_health_controller import SystemHealthController


@pytest.fixture
def system_health_model():
    """Fixture to initialize and clean up SystemHealthModel."""
    model = SystemHealthModel(udp_port=5001)
    yield model
    model.stop()


@pytest.fixture
def system_health_controller(system_health_model):
    """Fixture to initialize SystemHealthController."""
    controller = SystemHealthController(system_health_model)
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


def test_signal_emission(qtbot, system_health_controller, mock_udp_socket):
    # Define the test message for the left camera
    test_message = b'cam-left,50.0,30.0'
    mock_udp_socket(test_message)

    # Wait for the left camera signal
    with qtbot.waitSignal(system_health_controller.data_updated, timeout=100) as spy:
        system_health_controller.model._process_udp_data(test_message)

    # Ensure the signal was emitted correctly
    assert spy.signal_triggered, "Left camera signal was not emitted."
    assert spy.args == ["cam-left", 50.0, 30.0]

    # Verify data for the left camera
    assert system_health_controller.model.get_health_data('cam-left') == {
        'core_temp': 50.0,
        'cpu_usage': 30.0,
    }
