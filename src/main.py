from PySide6.QtWidgets import QApplication
import sys
from controller.system_health_controller import SystemHealthController
from model.system_health_model import SystemHealthModel
from view.system_health_view import MainWindow
import view.resources_rc  # Ensure the resources are imported

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Initialize model and controller
    model = SystemHealthModel(udp_port=5005)
    controller = SystemHealthController(model)

    # Initialize the view
    view = MainWindow(controller)
    view.show()

    sys.exit(app.exec())
