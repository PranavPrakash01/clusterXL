# connection_point.py
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QBrush, QPainter

class ConnectionPoint(QWidget):
    def __init__(self, parent, node_type, column=None):
        super().__init__(parent)
        self.setFixedSize(15, 15)  # Adjust the size of the circle widget
        self.is_active = False  # Changed from is_selected to is_active
        self.node_type = node_type
        self.column = column

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw a small grey or red circle in the center based on activation
        circle_radius = 5
        if self.is_active:  # Changed from is_selected to is_active
            painter.setBrush(QBrush(Qt.red))
        else:
            painter.setBrush(QBrush(Qt.gray))
        painter.drawEllipse(self.rect().center(), circle_radius, circle_radius)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Toggle the activation state
            previous_state = self.is_active  # Store the previous state
            self.is_active = not self.is_active  # Changed from is_selected to is_active
            # Trigger a repaint to update the color
            self.update()

            # Print the connection point information with the active state
            self.print_connection_point_info(previous_state)

        # Propagate the event to the parent
        super().mousePressEvent(event)

    def print_connection_point_info(self, previous_state):
        activation_state = "Activated" if self.is_active else "Deactivated"
        if self.node_type == "SingleSumNode":
            print(f"Connection Point: Single Input Sum Node [{activation_state}]")
        elif self.node_type == "AverageNode":
            print(f"Connection Point: Single Input Average Node [{activation_state}]")
        elif self.node_type == "Table":
            if self.column is not None:
                print(f"Connection Point: Table Column {self.column} [{activation_state}]")
