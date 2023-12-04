# table_widget.py
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt, QPoint

class TableWidget(QWidget):
    def __init__(self, rows, columns):
        super().__init__()

        self.rows = rows
        self.columns = columns

        self.is_dragging = False
        self.offset = QPoint()

        layout = QGridLayout(self)
        layout.setSpacing(0)  # Set spacing to 0 to reduce the distance between cells
        self.cells = [[QLineEdit(self) for _ in range(columns)] for _ in range(rows)]

        for row in range(rows):
            for col in range(columns):
                layout.addWidget(self.cells[row][col], row, col)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            new_position = self.mapToParent(event.pos() - self.offset)
            self.move(new_position)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False