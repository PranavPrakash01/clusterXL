# connection_point.py
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QBrush, QPainter

class ConnectionPoint(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedSize(15, 15)  # Adjust the size of the circle widget

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw a small grey circle in the center
        circle_radius = 5
        painter.setBrush(QBrush(Qt.gray))
        painter.drawEllipse(self.rect().center(), circle_radius, circle_radius)
