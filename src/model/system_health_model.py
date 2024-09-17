from PySide6.QtCore import QMetaObject, QObject, Signal, Slot, Qt, Q_ARG
import socket
import threading
import logging
import signal
import sys
import time
import psutil


class SystemHealthModel(QObject):
    data_received = Signal(str, float, float)  # Signal to notify when new data is received

    def __init__(self, udp_port=5001, timeout=1.0, buffer_size=128, retry_attempts=3):
        super().__init__()
        self._udp_port = udp_port
        self._timeout = timeout
        self._buffer_size = buffer_size
        self._retry_attempts = retry_attempts
        self._health_data = {}
        self._stop_event = threading.Event()
        self._sock = None

        self._udp_listener_thread = threading.Thread(target=self._listen_for_udp)
        self._udp_listener_thread.daemon = True
        self._udp_listener_thread.start()

        self._dashboard_data_thread = threading.Thread(target=self._get_dashboard_data)
        self._dashboard_data_thread.daemon = True
        self._dashboard_data_thread.start()

    def _get_dashboard_data(self):
        while not self._stop_event.is_set():
            component = 'dashboard'
            core_temp = 10 # psutil.sensors_temperatures()['cpu_thermal'][0].current
            cpu_usage = psutil.cpu_percent(interval=1)
            self.data_received.emit(component, core_temp, cpu_usage)
            time.sleep(10)

    def _listen_for_udp(self):
        """Listen for UDP packets and process them."""
        for attempt in range(self._retry_attempts):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                    self._sock = sock  # Store the socket for later closure
                    sock.settimeout(self._timeout)
                    sock.bind(('0.0.0.0', self._udp_port))
                    logging.info(f"UDP socket bound to port {self._udp_port} on attempt {attempt + 1}")

                    while not self._stop_event.is_set():
                        try:
                            data, _ = sock.recvfrom(self._buffer_size)
                            self._process_udp_data(data)
                        except socket.timeout:
                            continue  # Timeout to allow for checking running event
                        except Exception as e:
                            logging.error(f"Error receiving UDP packet: {e}")
            except OSError as e:
                logging.error(f"Failed to bind to port {self._udp_port} on attempt {attempt + 1}: {e}")
                if attempt == self._retry_attempts - 1:
                    logging.error(f"Maximum retry attempts reached. Could not bind to port {self._udp_port}")
                    return
                time.sleep(2)  # Wait before retrying
            else:
                break  # Successfully bound to port

        # Clean up the socket after the loop ends
        if self._sock:
            logging.info("Closing UDP socket")
            self._sock.close()
            self._sock = None

    def _process_udp_data(self, data):
        """Process incoming UDP data and emit signal."""
        try:
            data_str = data.decode('utf-8')
            parts = data_str.split(',')

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
            logging.error(f"Error processing data: {e}")

    def stop(self):
        """Stop listening and close all resources."""
        logging.info("Stopping UDP listener")
        self._stop_event.set()  # Signal the thread to stop
        if self._udp_listener_thread.is_alive():
            self._udp_listener_thread.join(timeout=1)  # Wait for the thread to exit
        if self._dashboard_data_thread.is_alive():
            self._dashboard_data_thread.join(timeout=1)  # Wait for the thread to exit
        if self._sock:
            self._sock.close()  # Ensure the socket is closed
            self._sock = None
        logging.info("SystemHealthModel stopped.")

    def get_health_data(self, component):
        """Retrieve health data for a specific component."""
        return self._health_data.get(component, {})

    def get_all_health_data(self):
        """Retrieve health data for all component."""
        return self._health_data

