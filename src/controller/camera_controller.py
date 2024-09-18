from PySide6.QtCore import QObject, Signal, Slot
import logging
import signal
import sys
import time

from src.model.camera_model import CameraModel
from src.view.camera_view_page import CameraView


class CameraController(QObject):
    def __init__(self, model: CameraModel, view: CameraView):
        super().__init__()
        self.model = model
        self.view = view


