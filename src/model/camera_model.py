from PySide6.QtCore import QMetaObject, QObject, Signal, Slot, Qt, Q_ARG
import threading


class CameraModel(QObject):
    data_received = Signal(str, float, float)  # Signal to notify when new data is received

    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def stop(self):
        """Stop listening and close all resources."""
        self._stop_event.set()  # Signal the thread to stop

