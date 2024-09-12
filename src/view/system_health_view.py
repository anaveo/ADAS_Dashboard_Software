from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from src.controller.system_health_controller import SystemHealthController
from src.model.system_health_model import SystemHealthModel

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Signal, Slot


class CameraWidget(QWidget):
    def __init__(self, camera_id, parent=None):
        super().__init__(parent)
        self.camera_id = camera_id

        # Create UI elements
        self.layout = QVBoxLayout()
        self.core_temp_label = QLabel("Core Temp: --")
        self.cpu_usage_label = QLabel("CPU Usage: --")
        self.memory_usage_label = QLabel("Memory Usage: --")

        self.layout.addWidget(self.core_temp_label)
        self.layout.addWidget(self.cpu_usage_label)
        self.layout.addWidget(self.memory_usage_label)
        self.setLayout(self.layout)

    @Slot(dict)
    def update_data(self, core_temp, cpu_usage, memory_usage):
        """Update the widget with the latest data for this camera."""
        self.core_temp_label.setText(f"Core Temp: {core_temp}")
        self.cpu_usage_label.setText(f"CPU Usage: {cpu_usage}")
        self.memory_usage_label.setText(f"Memory Usage: {memory_usage}")


class MainWindow(QMainWindow):
    def __init__(self, controller: SystemHealthController):
        super().__init__()

        # Create and set up the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create widgets for each camera
        self.camera_widget1 = CameraWidget(camera_id="camera1")
        self.camera_widget2 = CameraWidget(camera_id="camera2")

        # Add widgets to layout
        layout.addWidget(self.camera_widget1)
        layout.addWidget(self.camera_widget2)

        # Connect controller signals to widget slots
        controller.data_updated_cam_left.connect(self.update_view_cam_left)
        controller.data_updated_cam_right.connect(self.update_view_cam_right)

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
