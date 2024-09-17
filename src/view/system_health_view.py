from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QButtonGroup
from PySide6.QtCore import Signal, Slot
from src.view.generated_ui.main_window_ui import Ui_MainWindow

from src.view.camera_view_page import CameraView
from src.view.lane_view_page import LaneView
from src.view.diagnostic_view_page import DiagnosticView

from src.controller.system_health_controller import SystemHealthController

from src.model.system_health_model import SystemHealthModel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize models
        self.system_health_model = SystemHealthModel(udp_port=5005)
        # self.camera_model = CameraModel()  # Replace with actual model
        # self.driving_conditions_model = DrivingConditionsModel()  # Replace with actual model

        # Initialize controllers
        self.diagnostics_controller = SystemHealthController(model=self.system_health_model)
        # self.camera_controller = CameraController()
        # self.driving_conditions_controller = DrivingConditionsController()

        # Create and set up UI instance
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # UI Pages
        self.camera_page = None
        self.lane_page = None
        self.diagnostic_page = None

        # Load pages and set up navigation bar
        self._load_pages()
        self._init_navigation_bar()

        self.ui.pageStack.setCurrentWidget(self.camera_page)

    def _load_pages(self):
        # Initialize and load Camera Page
        self.camera_page = CameraView()
        self.ui.pageStack.addWidget(self.camera_page)

        # Initialize and load Lane Page
        self.lane_page = LaneView()
        self.ui.pageStack.addWidget(self.lane_page)

        # Initialize and load Diagnostic Page
        self.diagnostic_page = DiagnosticView(controller=self.diagnostics_controller)
        self.ui.pageStack.addWidget(self.diagnostic_page)

    def _init_navigation_bar(self):
        # Create a button group
        self.navigation_bar_button_group = QButtonGroup(self)
        self.navigation_bar_button_group.setExclusive(True)  # Only one button can be active at a time

        # Add buttons to the button group
        self.navigation_bar_button_group.addButton(self.ui.cameraViewButton)
        self.navigation_bar_button_group.addButton(self.ui.laneViewButton)
        self.navigation_bar_button_group.addButton(self.ui.diagnosticViewButton)

        # Connect buttons to show different pages in QStackedWidget
        self.ui.cameraViewButton.clicked.connect(lambda: self._show_page(0))  # Show camera view
        self.ui.laneViewButton.clicked.connect(lambda: self._show_page(1))  # Show lane view
        self.ui.diagnosticViewButton.clicked.connect(lambda: self._show_page(2))  # Show diagnostic view

        # Refresh data when diagnostic page opened
        # self.ui.diagnosticViewButton.clicked.connect(lambda: self.diagnostic_page.update_all_displays())  # Show page 3

    def _show_page(self, index):
        """Function to switch pages in the QStackedWidget"""
        self.ui.pageStack.setCurrentIndex(index)
