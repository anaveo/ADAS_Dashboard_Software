
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal, Slot
from src.view.generated_ui.camera_view_page_ui import Ui_CameraViewPage


class CameraView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, left_cam_port=5010, right_cam_port=5020)
        self.left_cam_port = left_cam_port
        self.right_cam_port = right_cam_port

        self.ui = Ui_CameraViewPage()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI with this MainWindow

        self.ui.leftCamStream.init_gstreamer(port=self.left_cam_port)
        self.ui.rightCamStream.init_gstreamer(port=self.right_cam_port)
