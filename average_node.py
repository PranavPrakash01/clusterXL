# average_node.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt, QPoint

class AverageNode(QWidget):
    def __init__(self):
        super().__init__()

        self.is_dragging = False
        self.offset = QPoint()

        # Create a layout for the widget
        layout = QVBoxLayout(self)

        # Title
        title_label = QLabel("AVERAGE")
        layout.addWidget(title_label)

        # Value
        self.cell_widget = QLineEdit("0")
        self.cell_widget.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # Right-align the text
        layout.addWidget(self.cell_widget)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.offset = event.pos()
        elif event.button() == Qt.RightButton:
            # Add logic for the right mouse button click if needed
            pass

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            new_position = self.mapToParent(event.pos() - self.offset)
            self.move(new_position)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False

    def mouseDoubleClickEvent(self, event):
        # Add logic for the double-click event if needed
        pass
