from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QCoreApplication, Qt, QRect
from PySide6.QtGui import QPainter, QColor
from src.view.generated_ui.linear_indicator_widget_ui import Ui_LinearIndicator  # Generated UI file


class LinearIndicator(QWidget, Ui_LinearIndicator):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Initialize instance variables
        self.high_val = 100
        self.low_val = 0
        self.blocks = 16  # Number of total blocks
        self.val = 0     # Initial value

    @staticmethod
    def _validate_inputs(high_val: int, low_val: int):
        """
        Validates the high and low value inputs.
        """
        if not isinstance(high_val, int) or not isinstance(low_val, int):
            raise ValueError("High and low values must be integers.")
        if low_val >= high_val:
            raise ValueError("Low value must be less than high value.")

    def update_value(self, new_val):
        """
        Updates the value and triggers a repaint.
        """
        if new_val > self.high_val:
            self.val = self.high_val
        elif new_val < self.low_val:
            self.val = self.low_val
        else:
            self.val = new_val

        # Trigger repaint only for the blocks area
        repaint_area = QRect(35, 25, 195, 16)
        self.update(repaint_area)  # Only repaint the area where blocks are drawn

    def update_fields(self, measure: str = None, high_str: str = None, low_str: str = None, high_val: int = None,
                      low_val: int = None):
        """
        Dynamically updates the widget values.
        Performs input validation before updating values.
        """
        # Validate new values if provided
        if high_val is not None and low_val is not None:
            self._validate_inputs(high_val, low_val)

        # Update the values if they are provided
        if measure:
            self.measureLabel.setText(QCoreApplication.translate("LinearIndicator", f"<html><head/><body><p><span style=\" font-size:12pt; color:#eeeeee;\">{measure}</span></p></body></html>", None))
        if high_str:
            self.highLabel.setText(QCoreApplication.translate("LinearIndicator", f"<html><head/><body><p><span style=\" font-size:11pt; color:#eeeeee;\">{high_str}</span></p></body></html>", None))
        if low_str:
            self.lowLabel.setText(QCoreApplication.translate("LinearIndicator", f"<html><head/><body><p><span style=\" font-size:12pt; color:#eeeeee;\">{low_str}</span></p></body></html>", None))
        if high_val is not None:
            self.high_val = high_val
        if low_val is not None:
            self.low_val = low_val

    def paintEvent(self, event):
        """
        Handles the painting of the widget.
        Draws the blue bar and fills it with white blocks based on the value.
        """
        # Create QPainter object
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the blue background bar
        painter.setBrush(QColor(30, 15, 250))  # Blue color
        painter.setPen(Qt.NoPen)
        painter.drawRect(35, 25, 184, 3)
        painter.setBrush(QColor(225, 15, 0))  # Blue color
        painter.drawRect(222, 25, 7, 3)
        painter.setBrush(QColor(70, 70, 100))  # Blue color
        painter.drawRect(35, 31, 194, 10)

        # Calculate how many blocks to fill based on the value
        filled_blocks = int(((self.val - self.low_val) / (self.high_val - self.low_val)) * self.blocks)

        # Draw the filled (white) blocks
        painter.setBrush(QColor(255, 255, 255))  # White color
        for i in range(filled_blocks):
            painter.drawRect((i * 10) + 38, 32, 8, 8)  # -2 for a small gap between blocks

        # End painting
        painter.end()
