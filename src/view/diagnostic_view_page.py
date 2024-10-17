from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal, Slot
from src.view.generated_ui.diagnostic_view_page_ui import Ui_DiagnosticViewPage

import logging
logger = logging.getLogger('view.diagnostic_view_page')


class DiagnosticView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_DiagnosticViewPage()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI with this widget

        self.health_data_cache = {}
        self.fault_data_cache = {}

        # Set up UI elements
        self.ui.dataDisplay_1.update_name("Left Camera")
        self.ui.dataDisplay_1.add_second_indicator()

        self.ui.dataDisplay_2.update_name("Dashboard")
        self.ui.dataDisplay_2.add_second_indicator()

        self.ui.dataDisplay_3.update_name("Right Camera")
        self.ui.dataDisplay_3.add_second_indicator()

        self.ui.dataDisplay_4.update_name("Power Module")
        self.ui.dataDisplay_5.update_name("Wheel Driver")

        # Initialize all displays
        self.update_all_displays()

    @Slot(str, float, float)
    def update_component_health_data(self, component_name: str, core_temp: float, cpu_usage: float):
        """Update health data and UI for a specific component."""
        self.health_data_cache[component_name] = {"core_temp": core_temp, "cpu_usage": cpu_usage}

        # Map component names to their corresponding UI elements
        ui_map = {
            "left-camera-health": self.ui.dataDisplay_1,
            "dashboard-health": self.ui.dataDisplay_2,
            "right-camera-health": self.ui.dataDisplay_3,
            "power-module-health": self.ui.dataDisplay_4,
            "wheel-driver-health": self.ui.dataDisplay_5
        }

        # Find the UI element for the given component
        data_display = ui_map.get(component_name)
        if data_display:
            data_display.update_indicators(core_temp, cpu_usage)
        else:
            logger.warning(f"Unknown component name: {component_name}")

    @Slot(str, str)
    def update_component_fault_data(self, component_name: str, fault: str):
        """Update fault data and UI for a specific component."""
        self.fault_data_cache[component_name] = {fault}

        # Map component names to their corresponding UI elements
        ui_map = {
            "left-camera-fault": self.ui.dataDisplay_1,
            "dashboard-fault": self.ui.dataDisplay_2,
            "right-camera-fault": self.ui.dataDisplay_3,
            "power-module-fault": self.ui.dataDisplay_4,
            "wheel-driver-fault": self.ui.dataDisplay_5
        }

        # Find the UI element for the given component
        data_display = ui_map.get(component_name)
        if data_display:
            data_display.update_error_message(fault)
        else:
            logger.warning(f"Unknown component name: {component_name}")

    @Slot()
    def update_all_displays(self):
        """Update all data displays with the cached data."""
        for component_name, data in self.health_data_cache.items():
            core_temp = data.get("core_temp", 0)
            cpu_usage = data.get("cpu_usage", 0)
            self.update_component_health_data(component_name, core_temp, cpu_usage)
