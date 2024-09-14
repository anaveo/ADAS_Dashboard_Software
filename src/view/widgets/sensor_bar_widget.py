from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt


class SensorBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.sensor_value = 0  # Initialize with default sensor value

    def set_sensor_value(self, value):
        self.sensor_value = value
        self.update()  # Repaint the widget with new sensor value

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.rect()
        bar_width = rect.width()
        bar_height = rect.height()

        # Draw background
        painter.setBrush(QColor("blue"))
        painter.drawRect(rect)

        # Draw white squares
        square_size = 10
        num_squares = bar_width // square_size
        for i in range(num_squares):
            if i < self.sensor_value:
                painter.setBrush(QColor("white"))
            else:
                painter.setBrush(QColor("blue"))  # To cover background
            painter.drawRect(i * square_size, 0, square_size, bar_height)
