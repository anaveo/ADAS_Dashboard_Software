from PySide6.QtCore import QObject, Signal, Slot
from src.model.system_health_model import SystemHealthModel
import logging
import signal
import sys
import time


class SystemHealthController(QObject):
    data_updated = Signal(str, float, float)  # Signal to notify when new data is received

    def __init__(self, model: SystemHealthModel):
        super().__init__()
        self.model = model

        self._device_lst = ['cam-left', 'cam-right', 'dashboard']

        # Connect model's signal to the controller slot
        self.model.data_received.connect(self.update_view)

    @Slot(str, float, float)
    def update_view(self, component, core_temp, cpu_usage):
        """Fetch health data from the model and emit signal to update the view."""
        if component in self._device_lst:
            self.data_updated.emit(component, core_temp, cpu_usage)

