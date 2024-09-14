from PySide6.QtCore import QMetaObject, QObject, Signal, Slot, Qt, Q_ARG
import socket
import threading
import logging
import signal
import sys
import time


class SystemHealthModel(QObject):
    data_received_cam_left = Signal(float, float)  # Signal to notify when new data is received
    data_received_cam_right = Signal(float, float)  # Signal to notify when new data is received

    def __init__(self, udp_port=5001, timeout=1.0, buffer_size=128, retry_attempts=3):
        super().__init__()
        self._udp_port = udp_port
        self._timeout = timeout
        self._buffer_size = buffer_size
        self._retry_attempts = retry_attempts
        self._camera_health_data = {}
        self._running = True
        self._sock = None
        self._device_lst = ['cam-left', 'cam-right']
        self._listener_thread = threading.Thread(target=self._listen_for_udp)
        self._listener_thread.daemon = True
        self._listener_thread.start()

    def _listen_for_udp(self):
        """Listen for UDP packets and process them."""
        for attempt in range(self._retry_attempts):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                    self._sock = sock  # Store the socket for later closure
                    sock.settimeout(self._timeout)
                    sock.bind(('0.0.0.0', self._udp_port))
                    logging.info(f"UDP socket bound to port {self._udp_port} on attempt {attempt + 1}")

                    while self._running:
                        try:
                            data, _ = sock.recvfrom(self._buffer_size)
                            self._process_data(data)
                        except socket.timeout:
                            continue  # Timeout to allow for checking _running flag
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

    def _process_data(self, data):
        """Process incoming UDP data and emit signal."""
        try:
            data_str = data.decode('utf-8')
            parts = data_str.split(',')

            if len(parts) != 3:
                raise ValueError("Invalid data format received")

            device_id, core_temp, cpu_usage = parts
            if device_id not in self._device_lst:
                raise ValueError(f"Unknown device: {device_id}")

            core_temp = float(core_temp)
            cpu_usage = float(cpu_usage)

            self._camera_health_data[device_id] = {
                'core_temp': core_temp,
                'cpu_usage': cpu_usage
            }

            # Safely emit the signal for the appropriate camera device
            if device_id == 'cam-left':
                self.data_received_cam_left.emit(core_temp, cpu_usage)
            elif device_id == 'cam-right':
                self.data_received_cam_right.emit(core_temp, cpu_usage)

        except Exception as e:
            logging.error(f"Error processing data: {e}")

    def stop(self):
        """Stop listening and close all resources."""
        logging.info("Stopping UDP listener")
        self._running = False
        if self._listener_thread.is_alive():
            self._listener_thread.join(timeout=1)  # Wait for the thread to exit
        if self._sock:
            self._sock.close()  # Ensure the socket is closed
            self._sock = None
        logging.info("SystemHealthModel stopped.")

    def get_camera_health_data(self, device_id):
        """Retrieve health data for a specific device."""
        return self._camera_health_data.get(device_id, {})

    def get_all_camera_health_data(self):
        """Retrieve health data for all devices."""
        return self._camera_health_data


# Optional: Handle shutdown signals to stop gracefully
def signal_handler():
    model.stop()
    sys.exit(0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    model = SystemHealthModel(udp_port=5001)
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)
    # Keep the main thread alive to handle signals
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        model.stop()
