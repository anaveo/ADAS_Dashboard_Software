import pytest
import asyncio
import socket
from unittest.mock import patch, MagicMock, ANY
from src.services.network_manager import NetworkManager
import logging.config
import json
import sys

pytestmark = pytest.mark.usefixtures("event_loop")

def setup_logging(config_path='logging_config.json'):
    with open(config_path, 'r') as f:
        config = json.load(f)
        logging.config.dictConfig(config)

def pytest_configure(config):
    setup_logging()

@pytest.fixture(scope="function")
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()

@pytest.fixture(scope="function")
def manager(event_loop):
    return NetworkManager(loop=event_loop)

@pytest.mark.asyncio
async def test_add_udp_port(manager):
    with patch.object(socket, 'socket') as mock_socket:
        mock_socket.return_value.bind.return_value = None
        mock_socket.return_value.setblocking.return_value = None
        await manager.add_udp_port(1234)
        assert 1234 in manager.udp_ports

@pytest.mark.asyncio
async def test_remove_udp_port(manager):
    with patch.object(socket, 'socket') as mock_socket:
        mock_socket.return_value.bind.return_value = None
        mock_socket.return_value.setblocking.return_value = None
        await manager.add_udp_port(1234)
        await manager.remove_udp_port(1234)
        assert 1234 not in manager.udp_ports

@pytest.mark.asyncio
async def test_register_udp_callback(manager):
    def callback(data, addr):
        pass
    manager.register_udp_callback(1234, callback)
    assert 1234 in manager.udp_callbacks

@pytest.mark.asyncio
async def test_unregister_udp_callback(manager):
    def callback(data, addr):
        pass
    manager.register_udp_callback(1234, callback)
    manager.unregister_udp_callback(1234, callback)
    assert 1234 not in manager.udp_callbacks

@pytest.mark.asyncio
async def test_register_tcp_callback(manager):
    def callback(data, addr):
        pass
    manager.register_tcp_callback(callback)
    assert callback in manager.tcp_callbacks

@pytest.mark.asyncio
async def test_unregister_tcp_callback(manager):
    def callback(data, addr):
        pass
    manager.register_tcp_callback(callback)
    manager.unregister_tcp_callback(callback)
    assert callback not in manager.tcp_callbacks

@pytest.mark.asyncio
async def test_start_tcp_server(manager):
    with patch.object(asyncio, 'start_server') as mock_start_server:
        await manager.start_tcp_server('localhost', 1234)
        mock_start_server.assert_called_once_with(
            ANY, 'localhost', 1234
        )

@pytest.mark.asyncio
async def test_stop(manager):
    with patch.object(asyncio, 'sleep') as mock_sleep:
        await manager.stop()
        mock_sleep.assert_called_once_with(1)
