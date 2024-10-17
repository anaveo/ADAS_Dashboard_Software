from PySide6.QtCore import QObject, Signal, Slot
import signal
import sys
import time

from src.model.diagnostic_model import DiagnosticModel
from src.view.diagnostic_view_page import DiagnosticView

import logging
logger = logging.getLogger('controller.diagnostic_controller')


class DiagnosticController(QObject):
    health_data_updated = Signal(str, float, float)  # Signal to notify when new health data is received
    fault_data_updated = Signal(str, str)  # Signal to notify when a fault is received

    def __init__(self, model: DiagnosticModel, view: DiagnosticView):
        super().__init__()
        self.model = model
        self.view = view

        # Connect model's signals to the controller slots
        self.model.health_data_received.connect(self.update_health_data)
        self.model.fault_data_received.connect(self.update_fault_data)

        # Connect controller's signals to the view's slots
        self.health_data_updated.connect(self.view.update_component_health_data)
        self.fault_data_updated.connect(self.view.update_component_fault_data)

    @Slot(str, float, float)
    def update_health_data(self, component, core_temp, cpu_usage):
        """Fetch health data from the model and emit signal to update the view."""
        try:
            if not isinstance(core_temp, (int, float)):
                raise ValueError(f"Invalid core_temp: {core_temp}")
            if not isinstance(cpu_usage, (int, float)):
                raise ValueError(f"Invalid cpu_usage: {cpu_usage}")

            self.health_data_updated.emit(component, core_temp, cpu_usage)
        except Exception as e:
            logger.error(f"Error updating health data: {e}")

    @Slot(str, str)
    def update_fault_data(self, component, fault):
        """Fetch fault data from the model and emit signal to update the view."""
        try:
            if not isinstance(fault, str):
                raise ValueError(f"Invalid fault message: {fault}")

            self.fault_data_updated.emit(component, fault)
        except Exception as e:
            logger.error(f"Error updating fault data: {e}")
