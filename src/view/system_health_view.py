import time

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from src.controller.system_health_controller import SystemHealthController
from src.model.system_health_model import SystemHealthModel

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QButtonGroup
from PySide6.QtCore import Signal, Slot
from src.view.generated_ui.main_window_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, controller: SystemHealthController):
        super(MainWindow, self).__init__()
        self.controller = controller

        self.ui = Ui_MainWindow()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI with this MainWindow

        # Create a button group
        self.navigation_bar_button_group = QButtonGroup(self)
        self.navigation_bar_button_group.setExclusive(True)  # Only one button can be active at a time

        # Add buttons to the button group
        self.navigation_bar_button_group.addButton(self.ui.cameraViewButton)
        self.navigation_bar_button_group.addButton(self.ui.laneViewButton)
        self.navigation_bar_button_group.addButton(self.ui.diagnosticViewButton)

        # Connect buttons to show different pages in QStackedWidget
        self.ui.cameraViewButton.clicked.connect(lambda: self.show_page(0))  # Show page 1
        self.ui.laneViewButton.clicked.connect(lambda: self.show_page(1))  # Show page 2
        self.ui.diagnosticViewButton.clicked.connect(lambda: self.show_page(2))  # Show page 3

        self._init_diagnostic_view()

    def _init_diagnostic_view(self):
        self.ui.dataDisplay_1.update_name("Left Camera")
        self.ui.dataDisplay_1.add_second_indicator()

        self.ui.dataDisplay_2.update_name("Dashboard")
        self.ui.dataDisplay_2.add_second_indicator()

        self.ui.dataDisplay_3.update_name("Right Camera")
        self.ui.dataDisplay_3.add_second_indicator()

        self.ui.dataDisplay_4.update_name("Power Module")
        self.ui.dataDisplay_5.update_name("Wheel Driver")

        self.controller.data_updated_cam_left.connect(self.ui.dataDisplay_1.update_indicators)
        self.controller.data_updated_cam_right.connect(self.ui.dataDisplay_3.update_indicators)

    def show_page(self, index):
        """Function to switch pages in the QStackedWidget"""
        self.ui.stackedWidget.setCurrentIndex(index)

        # # Create and set up the central widget and layout
        # central_widget = QWidget()
        # self.setCentralWidget(central_widget)
        # layout = QVBoxLayout()
        # central_widget.setLayout(layout)
        #
        # # Create widgets for each camera
        # self.camera_widget1 = CameraWidget(camera_id="camera1")
        # self.camera_widget2 = CameraWidget(camera_id="camera2")
        #
        # # Add widgets to layout
        # layout.addWidget(self.camera_widget1)
        # layout.addWidget(self.camera_widget2)
        #
        # # Connect controller signals to widget slots
        # controller.data_updated_cam_left.connect(self.update_view_cam_left)
        # controller.data_updated_cam_right.connect(self.update_view_cam_right)

    @Slot(float, float, float)
    def update_view_cam_left(self, core_temp, cpu_usage, memory_usage):
        """Fetch health data from the model and emit signal to update the view."""
        self.camera_widget1.update_data(core_temp, cpu_usage, memory_usage)

    @Slot(float, float, float)
    def update_view_cam_right(self, core_temp, cpu_usage, memory_usage):
        """Fetch health data from the model and emit signal to update the view."""
        self.camera_widget2.update_data(core_temp, cpu_usage, memory_usage)

    def update_all_widgets(self, data):
        """Update all camera widgets with the latest data."""
        if 'camera1' in data:
            self.camera_widget1.update_data(data)
        if 'camera2' in data:
            self.camera_widget2.update_data(data)
