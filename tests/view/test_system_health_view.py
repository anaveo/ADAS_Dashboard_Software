import pytest
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from src.controller.diagnostic_controller import DiagnosticController


# Example of a basic View class to represent camera data
class SystemHealthView(QWidget):
    def __init__(self, controller: DiagnosticController):
        super().__init__()
        self.controller = controller

        # Initialize the UI with labels for each camera
        self.cam_left_label = QLabel("Left Camera: N/A", self)
        self.cam_right_label = QLabel("Right Camera: N/A", self)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.cam_left_label)
        layout.addWidget(self.cam_right_label)
        self.setLayout(layout)

        # Connect the controller's signals to update the view
        self.controller.data_updated_cam_left.connect(self.update_left_camera_data)
        self.controller.data_updated_cam_right.connect(self.update_right_camera_data)

    def update_left_camera_data(self, core_temp, cpu_usage, memory_usage):
        """Update the left camera label with the received data."""
        self.cam_left_label.setText(f"Left Camera: Temp={core_temp}°C, CPU={cpu_usage}%, Memory={memory_usage}%")

    def update_right_camera_data(self, core_temp, cpu_usage, memory_usage):
        """Update the right camera label with the received data."""
        self.cam_right_label.setText(f"Right Camera: Temp={core_temp}°C, CPU={cpu_usage}%, Memory={memory_usage}%")


# Fixtures for setting up the controller and the view
@pytest.fixture
def system_health_view(diagnostic_controller):
    """Fixture to initialize SystemHealthView."""
    view = SystemHealthView(diagnostic_controller)
    return view


def test_view_updates_on_left_camera_signal(qtbot, diagnostic_controller, system_health_view, mock_udp_socket):
    """Test if the left camera label in the view is updated correctly when the signal is emitted."""
    test_message = b'cam-left,42.0,21.5,69.8'
    mock_udp_socket(test_message)

    # Wait for the left camera signal and check the view update
    with qtbot.waitSignal(diagnostic_controller.data_updated_cam_left, timeout=100):
        diagnostic_controller.model._process_udp_data(test_message)

    # Ensure the view is updated correctly
    assert system_health_view.cam_left_label.text() == "Left Camera: Temp=42.0°C, CPU=21.5%, Memory=69.8%"


def test_view_updates_on_right_camera_signal(qtbot, diagnostic_controller, system_health_view, mock_udp_socket):
    """Test if the right camera label in the view is updated correctly when the signal is emitted."""
    test_message = b'cam-right,50.0,30.0,70.0'
    mock_udp_socket(test_message)

    # Wait for the right camera signal and check the view update
    with qtbot.waitSignal(diagnostic_controller.data_updated_cam_right, timeout=100):
        diagnostic_controller.model._process_udp_data(test_message)

    # Ensure the view is updated correctly
    assert system_health_view.cam_right_label.text() == "Right Camera: Temp=50.0°C, CPU=30.0%, Memory=70.0%"


def test_view_no_update_when_no_signal(qtbot, diagnostic_controller, system_health_view):
    """Test that the view labels do not change when no signal is emitted."""

    # Verify that no updates occur when no signal is emitted
    assert system_health_view.cam_left_label.text() == "Left Camera: N/A"
    assert system_health_view.cam_right_label.text() == "Right Camera: N/A"


def test_view_updates_for_both_cameras(qtbot, diagnostic_controller, system_health_view, mock_udp_socket):
    """Test if both camera labels in the view are updated correctly when both signals are emitted."""

    # Simulate a message for the left camera
    test_message_left = b'cam-left,42.0,21.5,69.8'
    mock_udp_socket(test_message_left)
    with qtbot.waitSignal(diagnostic_controller.data_updated_cam_left, timeout=100):
        diagnostic_controller.model._process_udp_data(test_message_left)

    # Simulate a message for the right camera
    test_message_right = b'cam-right,50.0,30.0,70.0'
    mock_udp_socket(test_message_right)
    with qtbot.waitSignal(diagnostic_controller.data_updated_cam_right, timeout=100):
        diagnostic_controller.model._process_udp_data(test_message_right)

    # Ensure the view is updated for both cameras
    assert system_health_view.cam_left_label.text() == "Left Camera: Temp=42.0°C, CPU=21.5%, Memory=69.8%"
    assert system_health_view.cam_right_label.text() == "Right Camera: Temp=50.0°C, CPU=30.0%, Memory=70.0%"


def test_view_refresh_does_not_update_when_no_data(qtbot, diagnostic_controller, system_health_view):
    """Test that the view does not update if the controller refreshes with no data."""

    # Trigger a refresh with no data
    diagnostic_controller.refresh_device_data()

    # Ensure the view remains unchanged
    assert system_health_view.cam_left_label.text() == "Left Camera: N/A"
    assert system_health_view.cam_right_label.text() == "Right Camera: N/A"
