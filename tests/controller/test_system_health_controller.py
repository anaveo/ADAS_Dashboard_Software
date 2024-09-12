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


def test_signal_emission_for_right_camera(qtbot, system_health_controller, mock_udp_socket):
    """Test if the right camera signal is emitted correctly."""
    test_message = b'cam-right,45.0,23.5,67.8'
    mock_udp_socket(test_message)

    # Wait for the right camera signal
    with qtbot.waitSignal(system_health_controller.data_updated_cam_right, timeout=100) as spy_right:
        system_health_controller.model._process_data(test_message)

    # Wait for the left camera signal (if any)
    with qtbot.waitSignal(system_health_controller.data_updated_cam_left, raising=False, timeout=100) as spy_left:
        QCoreApplication.processEvents()

    # Ensure the right signal was emitted and left signal wasnt
    assert spy_right.signal_triggered, "Right camera signal was not emitted."
    assert not spy_left.signal_triggered, "Left camera signal was incorrectly emitted."

    core_temp, cpu_usage, memory_usage = spy_right.args

    assert core_temp == 45.0
    assert cpu_usage == 23.5
    assert memory_usage == 67.8


def test_signal_emission_for_left_camera(qtbot, system_health_controller, mock_udp_socket):
    """Test if the right camera signal is emitted correctly."""
    test_message = b'cam-left,42.0,21.5,69.8'
    mock_udp_socket(test_message)

    # Wait for the left camera signal
    with qtbot.waitSignal(system_health_controller.data_updated_cam_left, timeout=100) as spy_left:
        system_health_controller.model._process_data(test_message)

    # Wait for the right camera signal (if any)
    with qtbot.waitSignal(system_health_controller.data_updated_cam_right, raising=False, timeout=100) as spy_right:
        QCoreApplication.processEvents()

    # Ensure the left signal was emitted and right signal wasnt
    assert spy_left.signal_triggered, "Left camera signal was not emitted."
    assert not spy_right.signal_triggered, "Right camera signal was incorrectly emitted."

    core_temp, cpu_usage, memory_usage = spy_left.args

    assert core_temp == 42.0
    assert cpu_usage == 21.5
    assert memory_usage == 69.8


def test_refresh_device_data(qtbot, system_health_controller):
    """Test if the refresh_device_data slot emits the correct signals for both left and right cameras."""

    # Set mock data in the model
    system_health_controller.model._camera_health_data = {
        'cam-left': {'core_temp': 45.0, 'cpu_usage': 23.5, 'memory_usage': 67.8},
        'cam-right': {'core_temp': 50.0, 'cpu_usage': 30.0, 'memory_usage': 70.0}
    }

    # Wait for left and right camera signals
    with qtbot.waitSignal(system_health_controller.data_updated_cam_left, raising=False, timeout=100) as spy_left:
        with qtbot.waitSignal(system_health_controller.data_updated_cam_right, raising=False, timeout=100) as spy_right:
            system_health_controller.refresh_device_data()

    # Validate that both signals were emitted and check their arguments
    assert spy_left.signal_triggered, "Left camera signal was not emitted."
    assert spy_right.signal_triggered, "Right camera signal was not emitted."

    # Verify that both signals have the correct arguments
    assert spy_left.args == [45.0, 23.5, 67.8], f"Left camera signal args: {spy_left.args}"
    assert spy_right.args == [50.0, 30.0, 70.0], f"Right camera signal args: {spy_right.args}"


def test_no_signal_emission_with_no_data(qtbot, system_health_controller):
    """Test that no signals are emitted when there is no data in the model."""

    # Wait for left and right camera signals
    with qtbot.waitSignal(system_health_controller.data_updated_cam_left, raising=False, timeout=100) as spy_left:
        with qtbot.waitSignal(system_health_controller.data_updated_cam_right, raising=False, timeout=100) as spy_right:
            system_health_controller.refresh_device_data()

    # Validate that both signals were emitted and check their arguments
    assert not spy_left.signal_triggered, "Left camera signal was not emitted."
    assert not spy_right.signal_triggered, "Right camera signal was not emitted."

    # Verify that both signals have the correct arguments
    assert spy_left.args is None, f"Left camera signal args: {spy_left.args}"
    assert spy_right.args is None, f"Right camera signal args: {spy_right.args}"
