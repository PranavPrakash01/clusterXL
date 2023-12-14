# connection_point.py
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QBrush, QPainter

class ConnectionPoint(QWidget):
    def __init__(self, parent, node_type, column=None):
        super().__init__(parent)
        self.setFixedSize(15, 15)  # Adjust the size of the circle widget
        self.is_selected = False
        self.node_type = node_type
        self.column = column

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw a small grey or red circle in the center based on selection
        circle_radius = 5
        if self.is_selected:
            painter.setBrush(QBrush(Qt.red))
        else:
            painter.setBrush(QBrush(Qt.gray))
        painter.drawEllipse(self.rect().center(), circle_radius, circle_radius)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Toggle the selection state
            self.is_selected = not self.is_selected
            # Trigger a repaint to update the color
            self.update()

            # Print the connection point information
            self.print_connection_point_info()

        # Propagate the event to the parent
        super().mousePressEvent(event)

    def print_connection_point_info(self):
        if self.node_type == "SingleSumNode":
            print("Connection Point: Single Input Sum Node")
        elif self.node_type == "AverageNode":
            print("Connection Point: Single Input Average Node")
        elif self.node_type == "Table":
            if self.column is not None:
                print(f"Connection Point: Table Column {self.column}")
