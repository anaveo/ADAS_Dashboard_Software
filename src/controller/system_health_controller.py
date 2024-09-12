from PySide6.QtCore import QObject, Signal, Slot
from src.model.system_health_model import SystemHealthModel


class SystemHealthController(QObject):
    data_updated_cam_left = Signal(float, float, float)  # Signal to notify when new data is received
    data_updated_cam_right = Signal(float, float, float)  # Signal to notify when new data is received

    def __init__(self, model: SystemHealthModel):
        super().__init__()
        self.model = model

        # Connect model's signal to the controller slot
        self.model.data_received_cam_left.connect(self.update_view_cam_left)
        self.model.data_received_cam_right.connect(self.update_view_cam_right)

    @Slot(float, float, float)
    def update_view_cam_left(self, core_temp, cpu_usage, memory_usage):
        """Fetch health data from the model and emit signal to update the view."""
        self.data_updated_cam_left.emit(core_temp, cpu_usage, memory_usage)

    @Slot(float, float, float)
    def update_view_cam_right(self, core_temp, cpu_usage, memory_usage):
        """Fetch health data from the model and emit signal to update the view."""
        self.data_updated_cam_right.emit(core_temp, cpu_usage, memory_usage)

    @Slot(str)
    def refresh_device_data(self):
        """Fetch health data for a specific device and emit signal."""
        all_camera_data = self.model.get_all_camera_health_data()
        data_left_cam = all_camera_data.get('cam-left')
        data_right_cam = all_camera_data.get('cam-right')
        if data_left_cam is not None:
            core_temp = data_left_cam['core_temp']
            cpu_usage = data_left_cam['cpu_usage']
            memory_usage = data_left_cam['memory_usage']
            self.data_updated_cam_left.emit(core_temp, cpu_usage, memory_usage)
        if data_right_cam is not None:
            core_temp = data_right_cam['core_temp']
            cpu_usage = data_right_cam['cpu_usage']
            memory_usage = data_right_cam['memory_usage']
            self.data_updated_cam_right.emit(core_temp, cpu_usage, memory_usage)
