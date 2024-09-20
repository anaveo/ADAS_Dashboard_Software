from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QButtonGroup
from PySide6.QtCore import Signal, Slot
from src.view.generated_ui.main_window_ui import Ui_MainWindow

from src.view.widgets.camera_stream_widget import GStreamerWidget

class MainWindow(QMainWindow):
    def __init__(self, camera_page, lane_page, diagnostics_page):
        super(MainWindow, self).__init__()

        # Create and set up UI instance
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # UI Pages
        self.camera_page = camera_page
        self.lane_page = lane_page
        self.diagnostic_page = diagnostics_page

        # Load pages and set up navigation bar
        self._load_pages()
        self._init_navigation_bar()

        self.ui.pageStack.setCurrentWidget(self.camera_page)

    def _load_pages(self):
        self.ui.pageStack.addWidget(self.camera_page)
        self.ui.pageStack.addWidget(self.lane_page)
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
        self.ui.cameraViewButton.setChecked(True)  # Default page

        # Refresh data when diagnostic page opened
        # self.ui.diagnosticViewButton.clicked.connect(lambda: self.diagnostic_page.update_all_displays())  # Show page 3

    def _show_page(self, index):
        """Function to switch pages in the QStackedWidget"""
        self.ui.pageStack.setCurrentIndex(index)

        if index == 0:  # Video page is selected
            self.camera_page.left_cam_stream.start_stream()
        else:
            self.camera_page.left_cam_stream.stop_stream()
