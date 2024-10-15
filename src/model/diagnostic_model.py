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
    data_received = Signal(str, float, float)  # Signal to notify when new data is received

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
            self._net_manager = NetworkManager.get_instance()
            await self._net_manager.add_udp_port(self._diagnostic_udp_port)
            self._net_manager.register_udp_callback(self._diagnostic_udp_port, self._udp_callback)

            self._can_manager = CanManager.get_instance()
            self._can_manager.register_callback(self._can_callback)

            logger.info(f"Successfully started and registered on UDP port {self._diagnostic_udp_port}")
        except Exception as e:
            logger.error(f"Failed to start or register callback: {e}")
            await self.stop()

    def _get_dashboard_data(self):
        """
        Get dashboard health data every 10 seconds
        """
        while not self._stop_event.is_set():
            component = 'dashboard'
            core_temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
            cpu_usage = psutil.cpu_percent(interval=1)
            self.data_received.emit(component, core_temp, cpu_usage)
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
            self.data_received.emit(component, core_temp, cpu_usage)

        except Exception as e:
            logger.error(f"Error processing data: {e}")

    async def _can_callback(self, message):
        logger.info(f"Received CAN message: {message}")

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
                self._can_manager.unregister_callback(self._can_callback)

            logger.info("Successfully stopped DiagnosticModel")
        except Exception as e:
            logger.error(f"Failed to stop DiagnosticModel: {e}")

    def get_health_data(self, component):
        """Retrieve health data for a specific component."""
        return self._health_data.get(component, {})

    def get_all_health_data(self):
        """Retrieve health data for all component."""
        return self._health_data
