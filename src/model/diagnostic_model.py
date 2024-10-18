from PySide6.QtCore import QMetaObject, QObject, Signal, Slot, Qt, Q_ARG
import threading
import time
import psutil
from src.services.network_manager import NetworkManager
from src.services.can_manager import CanManager
import asyncio

import logging

logger = logging.getLogger('model.diagnostic_model')


class DiagnosticModel(QObject):
    health_data_received = Signal(str, float, float)  # Signal to notify when new health data is received
    fault_data_received = Signal(str, str)  # Signal to notify when a fault is received

    def __init__(self, diagnostic_port=5000):
        super().__init__()
        self._diagnostic_udp_port = diagnostic_port
        self._health_data = {}
        self._stop_event = threading.Event()

        self._net_manager = None
        self._can_manager = None
        self._dashboard_data_thread = None

    async def start(self):
        """
        Start the diagnostic model and register the UDP port for receiving health
        """
        try:
            # Start the data acquisition thread
            self._dashboard_data_thread = threading.Thread(target=self._get_dashboard_data, daemon=True)
            self._dashboard_data_thread.start()

            # Setup diagnostic UDP port
            self._net_manager = NetworkManager()
            await self._net_manager.add_udp_port(self._diagnostic_udp_port)
            self._net_manager.register_udp_callback(self._diagnostic_udp_port, self._udp_callback)

            self._can_manager = CanManager()

            # Register CAN message callbacks
            self._can_manager.register_callback_range_id(0x210, 0x260, self._device_status_can_callback)  # Health IDs
            self._can_manager.register_callback_range_id(0x310, 0x360, self._device_fault_can_callback)  # Fault IDs

            logger.info("Successfully started")
        except Exception as e:
            logger.error(f"Failed to start or register callbacks: {e}")
            await self.stop()

    def _get_dashboard_data(self):
        """
        Get dashboard health data every 10 seconds
        """
        while not self._stop_event.is_set():
            component = 'dashboard-health'
            core_temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
            cpu_usage = psutil.cpu_percent(interval=1)
            self.health_data_received.emit(component, core_temp, cpu_usage)

            # Send fault signal based on health conditions
            component = 'dashboard-fault'
            if 60 < core_temp <= 70:
                logger.warning("High temperature detected")
                self.fault_data_received.emit(component, 'THERMAL FAULT')
            elif core_temp > 70:
                logger.error("Critical temperature reached. Shutting down...")
                # TODO: Add stop here!
            elif cpu_usage > 90:
                logger.warning("High CPU usage detected")
                self.fault_data_received.emit(component, 'CPU OVERLOAD')
            else:
                self.fault_data_received.emit(component, '')

            time.sleep(10)

    def _udp_callback(self, data, addr):
        """
        Callback function to process the received data
        """
        try:
            parts = data.split(',')

            if len(parts) != 3:
                raise ValueError("Invalid data format received")

            component, core_temp, cpu_usage = parts
            if component not in ["cam-left", "cam-right"]:
                raise ValueError(f"Unknown component: {component}")

            core_temp = float(core_temp)
            cpu_usage = float(cpu_usage)

            self._health_data[component] = {
                'core_temp': core_temp,
                'cpu_usage': cpu_usage
            }

            # Safely emit the signal for the appropriate component
            self.health_data_received.emit(component, core_temp, cpu_usage)

        except Exception as e:
            logger.error(f"Error processing data: {e}")

    def _validate_can_message(self, id, message_info, message):

        # Look up the message ID in the message table
        if id not in self._can_manager.msg_table:
            logger.warning(f"CAN message ID {id} is not recognized")
            return False

        # Check if the message DLC matches the expected DLC
        if message.dlc != message_info['dlc']:
            logger.warning(f"Received CAN message {id} with unexpected DLC {message.dlc}")
            return False

        return True

    async def _device_status_can_callback(self, message):
        """
        Callback function to handle incoming CAN status messages and emit signals based on the message ID.
        """
        id = hex(message.arbitration_id)
        message_info = self._can_manager.msg_table[id]

        if self._validate_can_message(id, message_info, message):
            # Emit signals based on the description associated with the message ID
            self.health_data_received.emit(message_info['description'], message.data[0], message.data[1])
            logger.info(f"Signal emitted for CAN message ID {id}")

    async def _device_fault_can_callback(self, message):
        """
        Callback function to handle incoming CAN fault messages and emit signals based on the message ID.
        """
        id = hex(message.arbitration_id)
        message_info = self._can_manager.msg_table[id]

        if self._validate_can_message(id, message_info, message):
            # TODO: Fix/standardize fault messages
            fault_msgs = ["", "THERMAL FAULT", "OVERCURRENT FAULT", "OVERVOLTAGE FAULT", "UNDERVOLTAGE FAULT", "CPU OVERLOAD"]
            if message.data[0] > len(fault_msgs):
                logger.error(f"Invalid fault message index: {message.data[0]}")
                return
            device_name = message_info['description'].replace('-fault', '')
            logger.info(f"Fault message from {device_name}: {fault_msgs[message.data[0]]}")

            # Emit signals based on the description associated with the message ID
            self.fault_data_received.emit(message_info['description'], fault_msgs[message.data[0]])
            logger.info(f"Signal emitted for CAN message ID {id}")

    async def stop(self):
        """
        Stop the dashboard data thread and clean up the resources.
        """
        try:
            self._stop_event.set()

            # Wait for the thread to finish
            if self._dashboard_data_thread.is_alive():
                self._dashboard_data_thread.join(timeout=1)

            # Deregister or clean up any communication-related resources
            if self._net_manager:
                self._net_manager.unregister_udp_callback(self._diagnostic_udp_port, self._udp_callback)
                await self._net_manager.remove_udp_port(self._diagnostic_udp_port)
            if self._can_manager:
                self._can_manager.unregister_callback(self._device_status_can_callback)

            logger.info("Successfully stopped DiagnosticModel")
        except Exception as e:
            logger.error(f"Failed to stop DiagnosticModel: {e}")

    def get_health_data(self, component):
        """Retrieve health data for a specific component."""
        return self._health_data.get(component, {})

    def get_all_health_data(self):
        """Retrieve health data for all component."""
        return self._health_data
