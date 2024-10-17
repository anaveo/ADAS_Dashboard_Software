import asyncio
import logging
import json

# Models
from src.model.camera_model import CameraModel
from src.model.diagnostic_model import DiagnosticModel

# Views
from src.view.camera_view_page import CameraView
from src.view.lane_view_page import LaneView
from src.view.diagnostic_view_page import DiagnosticView

# Controllers
from src.controller.camera_controller import CameraController
from src.controller.diagnostic_controller import DiagnosticController
from src.controller.lane_controller import LaneController

# Communication managers
from src.services.network_manager import NetworkManager
from src.services.can_manager import CanManager

from src.view.main_window import MainWindow
import src.view.resources_rc  # Ensure resources are imported

logger = logging.getLogger('main_application')


class MainApplication:
    def __init__(self, config_path='../config/config.json', can_config_path='../config/can_config.json'):
        self.config = {}
        with open(config_path, 'r') as f:
            self.config = json.load(f)

        # Communication Managers
        self.net_manager = NetworkManager()
        self.can_manager = CanManager(can_config_path=can_config_path)

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

    async def init_mvc(self):
        try:

            # Initialize the models
            diagnostic_port = self.config["ports"]["left-cam"]["diagnostic"]

            self.camera_model = CameraModel()
            self.diagnostic_model = DiagnosticModel(diagnostic_port=diagnostic_port)

            # Initialize the views
            left_cam_port = self.config["ports"]["left-cam"]["stream"]
            right_cam_port = self.config["ports"]["right-cam"]["stream"]

            self.camera_view = CameraView(left_cam_port=left_cam_port, right_cam_port=right_cam_port)
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

            logger.info("MVC initialization complete.")

        except Exception as e:
            logger.error(f"Error during MVC initialization: {e}")
            await self.cleanup()

    async def init_comms_managers(self):
        # Start the NetworkManager
        await self.net_manager.start()

        # Start the CanManager and register shutdown CAN message
        await self.can_manager.start()
        self.can_manager.register_callback_single_id(message_id=0x100, callback=self.shutdown_callback)

    def run(self):
        if self.main_window:
            self.main_window.show()
        else:
            logger.error("MainWindow is not initialized.")
            raise RuntimeError("MainWindow is not initialized.")

    async def cleanup(self):
        """
        Cleanup method to ensure proper shutdown.
        """
        if self.diagnostic_model:
            await self.diagnostic_model.stop()  # Assuming there's a stop method to stop the model

        # Ensure proper cleanup of comms managers
        if self.net_manager:
            await self.net_manager.stop()
        if self.can_manager:
            await self.can_manager.stop()

        logger.info("Cleanup completed.")

    async def shutdown_callback(self, message):
        logger.info("Received shutdown command. Shutting down...")
        await self.cleanup()
        self.main_window.close()
        asyncio.get_event_loop().stop()
        logger.info("Shutdown complete.")
