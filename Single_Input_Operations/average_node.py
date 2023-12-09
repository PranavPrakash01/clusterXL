# average_node.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QMenu, QAction
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
        self.cell_widget.setReadOnly(True)  # Make the QLineEdit read-only
        self.cell_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.cell_widget.customContextMenuRequested.connect(self.show_context_menu)

        layout.addWidget(self.cell_widget)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.offset = event.pos()
        elif event.button() == Qt.RightButton:
            self.show_context_menu(event.pos())

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            new_position = self.mapToParent(event.pos() - self.offset)
            self.move(new_position)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False

    def show_context_menu(self, pos):
        menu = QMenu(self)

        delete_action = menu.addAction("Delete")
        action = menu.exec_(self.mapToGlobal(pos))

        if action == delete_action:
            self.delete_node()

    def delete_node(self):
        self.setParent(None)
        self.deleteLater()
