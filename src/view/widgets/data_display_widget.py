from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import QCoreApplication, QSize, Slot
from src.view.generated_ui.data_display_widget_ui import Ui_DataDisplay
from src.view.widgets.linear_indicator_widget import LinearIndicator


class DataDisplay(QWidget, Ui_DataDisplay):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.indicator_1.update_fields("Temp", "H", "C", 85, 30)
        self.indicator_2 = None

    def update_name(self, name):
        self.nameLabel.setText(name)
        self.nameLabel.setText(QCoreApplication.translate("DataDisplay",
                                                          f"<html><head/><body><p><span style=\" color:#eeeeee;\">{name}</span></p></body></html>",
                                                          None))

    @Slot(float, float)
    def update_indicators(self, core_temp, cpu_usage):
        self.indicator_1.update_value(core_temp)
        if self.indicator_2 is not None and cpu_usage is not None:
            self.indicator_2.update_value(cpu_usage)

    def add_second_indicator(self):
        self.resize(265, 235)
        self.errorLabel.setGeometry(0, 190, 265, 25)
        self.indicator_2 = LinearIndicator(self)
        self.indicator_2.setGeometry(0, 130, 265, 60)
        self.indicator_2.update_fields("CPU", "H", "L", 100, 0)
