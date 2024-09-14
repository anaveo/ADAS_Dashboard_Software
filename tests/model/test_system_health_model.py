import pytest
from PySide6.QtCore import QCoreApplication
from src.model.system_health_model import SystemHealthModel


@pytest.fixture
def system_health_model():
    """Fixture to initialize and clean up SystemHealthModel."""
    model = SystemHealthModel(udp_port=5001)
    yield model
    model.stop()


@pytest.fixture
def mock_udp_socket(monkeypatch):
    """Fixture to mock the UDP socket with a configurable message."""

    def _mock_udp_socket(message: bytes):
        """Configure the mock socket with the provided message."""

        def mock_recvfrom(*args, **kwargs):
            return message, ('localhost', 5001)

        monkeypatch.setattr('socket.socket.recvfrom', mock_recvfrom)

    return _mock_udp_socket


def test_signal_emission_for_left_camera(qtbot, system_health_model, mock_udp_socket):
    # Define the test message for the left camera
    test_message = b'cam-left,50.0,30.0'
    mock_udp_socket(test_message)

    # Wait for the left camera signal
    with qtbot.waitSignal(system_health_model.data_received_cam_left, timeout=100) as spy_left:
        system_health_model._process_data(test_message)

    # Wait for right camera signal (if any)
    with qtbot.waitSignal(system_health_model.data_received_cam_right, raising=False, timeout=100) as spy_right:
        QCoreApplication.processEvents()

    # Ensure the left signal was emitted and right signal wasnt
    assert spy_left.signal_triggered, "Left camera signal was not emitted."
    assert not spy_right.signal_triggered, "Right camera signal was incorrectly emitted."

    # Verify data for the left camera
    assert system_health_model.get_camera_health_data('cam-left') == {
        'core_temp': 50.0,
        'cpu_usage': 30.0,
    }


def test_signal_emission_for_right_camera(qtbot, system_health_model, mock_udp_socket):
    # Define the test message for the left camera
    test_message = b'cam-right,52.0,31.0'
    mock_udp_socket(test_message)

    # Wait for the right camera signal
    with qtbot.waitSignal(system_health_model.data_received_cam_right, timeout=100) as spy_right:
        system_health_model._process_data(test_message)

    # Wait for left camera signal (if any)
    with qtbot.waitSignal(system_health_model.data_received_cam_left, raising=False, timeout=100) as spy_left:
        QCoreApplication.processEvents()

    # Ensure the right signal was emitted and left signal wasnt
    assert spy_right.signal_triggered, "Right camera signal was not emitted."
    assert not spy_left.signal_triggered, "Left camera signal was incorrectly emitted."

    # Verify data for the left camera
    assert system_health_model.get_camera_health_data('cam-right') == {
        'core_temp': 52.0,
        'cpu_usage': 31.0,
    }


def test_signal_emission_for_both_cameras(qtbot, system_health_model, mock_udp_socket):
    # Define the test message for the left camera
    test_message_left = b'cam-left,52.1,31.1'
    mock_udp_socket(test_message_left)
    # Define the test message for the left camera
    test_message_right = b'cam-right,51.1,36.1'
    mock_udp_socket(test_message_right)

    # Wait for the left camera signal
    with qtbot.waitSignal(system_health_model.data_received_cam_left, timeout=100) as spy_left:
        system_health_model._process_data(test_message_left)

    # Wait for the right camera signal
    with qtbot.waitSignal(system_health_model.data_received_cam_right, timeout=100) as spy_right:
        system_health_model._process_data(test_message_right)

    # Ensure both signals were emitted
    assert spy_left.signal_triggered, "Left camera signal was not emitted."
    assert spy_right.signal_triggered, "Right camera signal was not emitted."

    # Verify data for the left camera
    assert system_health_model.get_camera_health_data('cam-left') == {
        'core_temp': 52.1,
        'cpu_usage': 31.1,
    }
    # Verify data for the right camera
    assert system_health_model.get_camera_health_data('cam-right') == {
        'core_temp': 51.1,
        'cpu_usage': 36.1,
    }


def test_get_all_camera_health_data(system_health_model):
    """Test retrieval of all health data."""
    # Mock data
    system_health_model._camera_health_data = {
        'cam-left': {
            'core_temp': 45.0,
            'cpu_usage': 23.5,
        },
        'cam-right': {
            'core_temp': 50.0,
            'cpu_usage': 30.0,
        }
    }

    # Get all health data
    result = system_health_model.get_all_camera_health_data()

    # Verify the result
    expected_data = {
        'cam-left': {
            'core_temp': 45.0,
            'cpu_usage': 23.5,
        },
        'cam-right': {
            'core_temp': 50.0,
            'cpu_usage': 30.0,
        }
    }
    assert result == expected_data, "All camera health data different from expected"


def test_get_camera_health_data(system_health_model):
    """Test retrieval of health data for a specific device."""
    # Mock data
    system_health_model._camera_health_data = {
        'cam-right': {
            'core_temp': 45.0,
            'cpu_usage': 23.5,
        }
    }

    # Get data for a specific device
    result = system_health_model.get_camera_health_data('cam-right')

    # Verify the result
    expected_data = {
        'core_temp': 45.0,
        'cpu_usage': 23.5,
    }
    assert result == expected_data, "Camera health data different from expected"


def test_error_handling_bad_id(system_health_model):
    """Test error handling in data processing."""
    # Define the test message for the left camera
    bad_id_data = 'device1,45.0,23.5'

    # Simulate receiving invalid data
    system_health_model._process_data(bad_id_data.encode('utf-8'))

    # Verify that invalid data does not crash the model
    assert system_health_model.get_all_camera_health_data() == {}


def test_error_handling_bad_data(system_health_model):
    """Test error handling in data processing."""
    # Define the test message for the left camera
    invalid_data = 'cam-left,45.0'

    # Simulate receiving invalid data
    system_health_model._process_data(invalid_data.encode('utf-8'))

    # Verify that invalid data does not crash the model
    assert system_health_model.get_all_camera_health_data() == {}
