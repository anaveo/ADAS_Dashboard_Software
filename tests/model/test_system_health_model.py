import pytest
import time
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
    with qtbot.waitSignal(system_health_model.data_received, timeout=100) as spy:
        system_health_model._process_udp_data(test_message)

    # Ensure the signal was emitted correctly
    assert spy.signal_triggered, "Left camera signal was not emitted."
    assert spy.args == ["cam-left", 50.0, 30.0]

    # Verify data for the left camera
    assert system_health_model.get_health_data('cam-left') == {
        'core_temp': 50.0,
        'cpu_usage': 30.0,
    }


def test_signal_emission_for_right_camera(qtbot, system_health_model, mock_udp_socket):
    # Define the test message for the left camera
    test_message = b'cam-right,52.0,31.0'
    mock_udp_socket(test_message)

    # Wait for the right camera signal
    with qtbot.waitSignal(system_health_model.data_received, timeout=100) as spy:
        system_health_model._process_udp_data(test_message)

    # Ensure the right signal was emitted and left signal wasnt
    assert spy.signal_triggered, "Right camera signal was not emitted."
    assert spy.args == ["cam-right", 52.0, 31.0]

    # Verify data for the right camera
    assert system_health_model.get_health_data('cam-right') == {
        'core_temp': 52.0,
        'cpu_usage': 31.0,
    }


def test_signal_emission_for_dashboard(qtbot, system_health_model):
    # Wait for the right camera signal
    with qtbot.waitSignal(system_health_model.data_received, timeout=12000) as spy:
        time.sleep(1)

    # Ensure the right signal was emitted and left signal wasnt
    assert spy.signal_triggered, "Dashboard signal was not emitted."
    assert spy.args[0] == "dashboard"

    # Verify data for the right camera
    assert system_health_model.get_health_data('cam-right') is not None


def test_get_all_health_data(system_health_model):
    """Test retrieval of all health data."""
    # Mock data
    system_health_model._health_data = {
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
    result = system_health_model.get_all_health_data()

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


def test_get_health_data(system_health_model):
    """Test retrieval of health data for a specific device."""
    # Mock data
    system_health_model._health_data = {
        'cam-right': {
            'core_temp': 45.0,
            'cpu_usage': 23.5,
        }
    }

    # Get data for a specific device
    result = system_health_model.get_health_data('cam-right')

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
    system_health_model._process_udp_data(bad_id_data.encode('utf-8'))

    # Verify that invalid data does not crash the model
    assert system_health_model.get_all_health_data() == {}


def test_error_handling_bad_data(system_health_model):
    """Test error handling in data processing."""
    # Define the test message for the left camera
    invalid_data = 'cam-left,45.0'

    # Simulate receiving invalid data
    system_health_model._process_udp_data(invalid_data.encode('utf-8'))

    # Verify that invalid data does not crash the model
    assert system_health_model.get_all_health_data() == {}
