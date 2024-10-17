import pytest
import asyncio
from unittest.mock import patch, MagicMock, AsyncMock
from src.services.can_manager import CanManager


@pytest.fixture
def event_loop():
    """Create an asyncio event loop for testing."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def can_manager(event_loop):
    return CanManager(loop=event_loop)


@pytest.mark.asyncio
async def test_start_can_manager(can_manager):
    """Test the start method of CanManager."""
    with patch('src.services.can_manager.os.system') as mock_os, \
         patch('src.services.can_manager.can.ThreadSafeBus') as mock_bus:
        # Simulate the CAN bus being set up
        mock_os.return_value = 0  # Simulate os.system() success
        mock_bus.return_value = MagicMock()

        await can_manager.start(bitrate=500000, interface='vcan0')

        # Check if the CAN bus was started with the correct arguments
        mock_os.assert_any_call('sudo ip link set vcan0 type can bitrate 500000')
        mock_os.assert_any_call('sudo ifconfig vcan0 up')

        # Check if the ThreadSafeBus was created
        assert mock_bus.called
        assert can_manager.is_running is True


@pytest.mark.asyncio
async def test_stop_can_manager(can_manager):
    """Test the stop method of CanManager."""
    with patch('src.services.can_manager.os.system') as mock_os:
        can_manager.is_running = True

        await can_manager.stop(interface='vcan0')

        # Check if the CAN bus was stopped
        mock_os.assert_called_with('sudo ifconfig vcan0 down')
        assert can_manager.is_running is False


# @pytest.mark.asyncio
# async def test_read_can_messages_with_no_message(can_manager):
#     """Test read_can_messages when no messages are received."""
#
#     # Use AsyncMock to allow await on mocked coroutine functions
#     mock_recv = AsyncMock(return_value=None)
#
#     with patch('src.services.can_manager.can.ThreadSafeBus.recv', mock_recv), \
#          patch('src.services.can_manager.asyncio.sleep', return_value=None):
#
#         can_manager.is_running = True
#
#         # This will allow the read_can_messages method to stop after a short time
#         timeout_duration = 0.1  # Set a timeout for the test
#         start_time = asyncio.get_event_loop().time()
#
#         # Start reading CAN messages
#         await can_manager.read_can_messages()
#
#         # Check if the method runs for a limited time
#         elapsed_time = asyncio.get_event_loop().time() - start_time
#         assert elapsed_time < timeout_duration, "read_can_messages ran too long"
#
#         # Assert that recv was called at least once
#         assert mock_recv.call_count > 0, "recv was not called"
#
#         # Since the function is designed to run forever, we will assert that no errors occurred
#         assert True  # If no exception occurs, the test passes


@pytest.mark.asyncio
async def test_dispatch_message_with_registered_callback(can_manager):
    """Test dispatching a CAN message to a registered callback."""
    callback = MagicMock()

    # Register a callback for message ID 0x200
    can_manager.register_callback_single_id(0x200, callback)

    # Create a mock CAN message
    mock_message = MagicMock()
    mock_message.arbitration_id = 0x200
    mock_message.data = b'\x01\x02'

    # Dispatch the message
    await can_manager.dispatch_message(mock_message)

    # Assert the callback was called with the message
    callback.assert_called_once_with(mock_message)


@pytest.mark.asyncio
async def test_dispatch_message_with_no_registered_callback(can_manager, caplog):
    """Test dispatching a CAN message with no registered callback."""
    # Create a mock CAN message with an ID that has no registered callback
    mock_message = MagicMock()
    mock_message.arbitration_id = 0x300

    with caplog.at_level('WARNING'):
        # Dispatch the message
        await can_manager.dispatch_message(mock_message)

        # Check that a warning was logged for no callback
        assert "No callback registered for CAN message ID 768" in caplog.text


@pytest.mark.asyncio
async def test_register_callback_range_id(can_manager):
    """Test registering a callback for a range of CAN message IDs."""
    callback = MagicMock()

    # Register a callback for message IDs 0x200 to 0x202
    can_manager.register_callback_range_id(0x200, 0x202, callback)

    # Assert that the callback is registered for the correct IDs
    assert 0x200 in can_manager.id_callback_map
    assert 0x201 in can_manager.id_callback_map
    assert 0x202 in can_manager.id_callback_map


@pytest.mark.asyncio
async def test_unregister_callback(can_manager):
    """Test unregistering a callback."""
    callback = MagicMock()

    # Register and then unregister a callback
    can_manager.register_callback_single_id(0x200, callback)
    can_manager.unregister_callback(callback)

    # Assert that the callback is unregistered
    assert 0x200 not in can_manager.id_callback_map
    assert callback not in can_manager.callback_id_map


@pytest.mark.asyncio
async def test_send_can_message(can_manager):
    """Test sending a CAN message."""

    # Mock the can.Message to ensure it's created correctly
    with patch('src.services.can_manager.can.Message') as mock_message, \
         patch('src.services.can_manager.can.ThreadSafeBus.send') as mock_send:

        # Create a mock CAN message object
        mock_message_instance = MagicMock()
        mock_message.return_value = mock_message_instance

        # Define the attributes for the mock CAN message
        mock_message_instance.arbitration_id = 0x200
        mock_message_instance.data = b'\x01\x02'

        # Send a CAN message with ID 0x200
        await can_manager.send_can_message(0x200, b'\x01\x02', interface='vcan0')

        # Check that the CAN message was created with the correct parameters
        mock_message.assert_called_once_with(arbitration_id=0x200, data=b'\x01\x02', is_extended_id=False)

        # Check that the send method was called with the correct message
        mock_send.assert_called_once_with(mock_message_instance)

