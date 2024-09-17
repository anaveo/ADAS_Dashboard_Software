from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal, Slot
from src.view.generated_ui.diagnostic_view_page_ui import Ui_DiagnosticViewPage
from src.controller.system_health_controller import SystemHealthController

class DiagnosticView(QWidget):
    def __init__(self, controller: SystemHealthController, parent=None):
        super().__init__(parent)

        # Initialize controller
        self.controller = controller

        self.ui = Ui_DiagnosticViewPage()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI with this widget

        self.data_cache = {}

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

        # Connect controller signals to slots
        self.controller.data_updated.connect(self.update_component_data)

    @Slot(str, float, float)
    def update_component_data(self, component_name: str, core_temp: float, cpu_usage: float):
        """Update data and UI for a specific component."""
        self.data_cache[component_name] = {"core_temp": core_temp, "cpu_usage": cpu_usage}

        # Map component names to their corresponding UI elements
        ui_map = {
            "cam-left": self.ui.dataDisplay_1,
            "dashboard": self.ui.dataDisplay_2,
            "cam-right": self.ui.dataDisplay_3,
            "power-module": self.ui.dataDisplay_4,
            "wheel-driver": self.ui.dataDisplay_5
        }

        # Find the UI element for the given component
        data_display = ui_map.get(component_name)
        if data_display:
            data_display.update_indicators(core_temp, cpu_usage)
        else:
            logging.warning(f"Unknown component name: {component_name}")

    @Slot()
    def update_all_displays(self):
        """Update all data displays with the cached data."""
        for component_name, data in self.data_cache.items():
            core_temp = data.get("core_temp", 0)
            cpu_usage = data.get("cpu_usage", 0)
            self.update_component_data(component_name, core_temp, cpu_usage)
