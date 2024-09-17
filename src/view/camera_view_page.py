
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal, Slot
from src.view.generated_ui.camera_view_page_ui import Ui_CameraViewPage


class CameraView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_CameraViewPage()  # Create an instance of the UI class
        self.ui.setupUi(self)  # Set up the UI with this MainWindow

