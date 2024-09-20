import asyncio
import logging
import json

# Models
from model.camera_model import CameraModel
from model.diagnostic_model import DiagnosticModel

# Views
from view.camera_view_page import CameraView
from view.lane_view_page import LaneView
from view.diagnostic_view_page import DiagnosticView

# Controllers
from controller.camera_controller import CameraController
from controller.diagnostic_controller import DiagnosticController
from controller.lane_controller import LaneController

from view.main_window import MainWindow
import view.resources_rc  # Ensure resources are imported
from services.communication_manager import CommunicationManager  # Import CommunicationManager

logger = logging.getLogger('main_application')


class MainApplication:
    def __init__(self, config_path='../config/config.json'):
        self.config = {}
        with open(config_path, 'r') as f:
            self.config = json.load(f)

        # Models
        self.camera_model = None
        self.diagnostic_model = None

        # Views
        self.camera_view = None
        self.lane_view = None
        self.diagnostic_view = None

        # Controllers
        self.camera_controller = None
        self.lane_controller = None
        self.diagnostic_controller = None

        # Main Window
        self.main_window = None

        # Initialize CommunicationManager for handling UDP communication
        self.comm_manager = CommunicationManager()

    async def init_mvc(self):
        try:
            # Initialize the models
            self.camera_model = CameraModel()
            self.diagnostic_model = DiagnosticModel(udp_port=self.config.get('udp_port', 5005))

            # Initialize the views
            self.camera_view = CameraView()
            self.lane_view = LaneView()
            self.diagnostic_view = DiagnosticView()

            # Initialize the controllers, passing both models and views
            self.camera_controller = CameraController(model=self.camera_model, view=self.camera_view)
            self.lane_controller = LaneController(model=self.camera_model, view=self.lane_view)
            self.diagnostic_controller = DiagnosticController(model=self.diagnostic_model, view=self.diagnostic_view)

            # Initialize the main window with the created views
            self.main_window = MainWindow(camera_page=self.camera_view, lane_page=self.lane_view,
                                          diagnostics_page=self.diagnostic_view)

            # Start the diagnostic model
            await self.diagnostic_model.start()

            # Start the CommunicationManager
            await self.comm_manager.start()

            logger.info("MVC initialization complete.")

        except Exception as e:
            logger.error(f"Error during MVC initialization: {e}")
            await self.cleanup()

    def run(self):
        if self.main_window:
            self.main_window.show()
        else:
            logger.error("MainWindow is not initialized.")

    async def cleanup(self):
        """
        Cleanup method to ensure proper shutdown.
        """
        if self.diagnostic_model:
            await self.diagnostic_model.stop()  # Assuming there's a stop method to stop the model

        if self.comm_manager:
            await self.comm_manager.stop()  # Ensure proper cleanup of communication manager

        logger.info("Cleanup completed.")
