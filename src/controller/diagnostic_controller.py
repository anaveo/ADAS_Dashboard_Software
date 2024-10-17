from PySide6.QtCore import QObject, Signal, Slot
import signal
import sys
import time

from src.model.diagnostic_model import DiagnosticModel
from src.view.diagnostic_view_page import DiagnosticView

import logging
logger = logging.getLogger('controller.diagnostic_controller')


class DiagnosticController(QObject):
    data_updated = Signal(str, float, float)  # Signal to notify when new data is received

    def __init__(self, model: DiagnosticModel, view: DiagnosticView):
        super().__init__()
        self.model = model
        self.view = view

        # Connect model's signal to the controller slot
        self.model.data_received.connect(self.update_view)

        # Connect controller's signal to the view's slot
        self.data_updated.connect(self.view.update_component_data)

    @Slot(str, float, float)
    def update_view(self, component, core_temp, cpu_usage):
        """Fetch health data from the model and emit signal to update the view."""
        try:
            if not isinstance(core_temp, (int, float)):
                raise ValueError(f"Invalid core_temp: {core_temp}")
            if not isinstance(cpu_usage, (int, float)):
                raise ValueError(f"Invalid cpu_usage: {cpu_usage}")

            self.data_updated.emit(component, core_temp, cpu_usage)
        except Exception as e:
            logger.error(f"Error updating view: {e}")

