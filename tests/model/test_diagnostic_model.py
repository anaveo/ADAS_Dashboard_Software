import pytest
import asyncio
from unittest.mock import patch, MagicMock
from src.model.diagnostic_model import DiagnosticModel
from src.services.network_manager import NetworkManager
import time
import psutil

@pytest.fixture
def diagnostic_model():
    model = DiagnosticModel(udp_port=5001)
    yield model
    model.stop()


@pytest.mark.asyncio
async def test_get_dashboard_data(diagnostic_model):
    # Create a mock function and connect it to the health_data_received signal
    mock_function = MagicMock()
    diagnostic_model.health_data_received.connect(mock_function)

    with patch.object(asyncio, 'sleep') as mock_sleep, \
         patch.object(psutil, 'cpu_percent', return_value=30.0), \
         patch.object(psutil.sensors_temperatures, 'cpu_thermal', return_value=[MagicMock(current=10.0)]):
        diagnostic_model._get_dashboard_data()
        mock_sleep.assert_called_once_with(10)

    # Assert that the mock function was called with the correct arguments
    mock_function.assert_called_once_with('dashboard', 10.0, 30.0)


def test_udp_callback(diagnostic_model):
    data = b'cam-left,50.0,30.0'
    addr = ('localhost', 5001)

    # Create a mock function and connect it to the health_data_received signal
    mock_function = MagicMock()
    diagnostic_model.health_data_received.connect(mock_function)

    # Call the _udp_callback method, which should emit the health_data_received signal
    diagnostic_model._udp_callback(data, addr)

    # Assert that the mock function was called with the correct arguments
    mock_function.assert_called_once_with('cam-left', 50.0, 30.0)

    # Assert that the health data was updated correctly
    assert diagnostic_model.get_health_data('cam-left') == {
        'core_temp': 50.0,
        'cpu_usage': 30.0,
    }


def test_stop(diagnostic_model):
    with patch.object(NetworkManager, 'remove_udp_port') as mock_remove_udp_port, \
            patch.object(NetworkManager, 'unregister_udp_callback') as mock_unregister_udp_callback:
        diagnostic_model.stop()
        mock_remove_udp_port.assert_called_once_with(5001)
        mock_unregister_udp_callback.assert_called_once()


def test_get_health_data(diagnostic_model):
    diagnostic_model._health_data = {
        'cam-left': {
            'core_temp': 50.0,
            'cpu_usage': 30.0,
        }
    }
    assert diagnostic_model.get_health_data('cam-left') == {
        'core_temp': 50.0,
        'cpu_usage': 30.0,
    }


def test_get_all_health_data(diagnostic_model):
    diagnostic_model._health_data = {
        'cam-left': {
            'core_temp': 50.0,
            'cpu_usage': 30.0,
        },
        'cam-right': {
            'core_temp': 52.0,
            'cpu_usage': 31.0,
        }
    }
    assert diagnostic_model.get_all_health_data() == {
        'cam-left': {
            'core_temp': 50.0,
            'cpu_usage': 30.0,
        },
        'cam-right': {
            'core_temp': 52.0,
            'cpu_usage': 31.0,
        }
    }
