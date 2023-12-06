# table_widget.py
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QMenu, QInputDialog
from PyQt5.QtCore import Qt, QPoint

class TableWidget(QWidget):
    def __init__(self, rows, columns):
        super().__init__()

        self.rows = rows
        self.columns = columns

        self.is_dragging = False
        self.offset = QPoint()

        # Keep track of cell data
        self.cell_data = [['' for _ in range(columns)] for _ in range(rows)]

        layout = QGridLayout(self)
        layout.setSpacing(0)  # Set spacing to 0 to reduce the distance between cells
        self.cells = [[QLineEdit(self) for _ in range(columns)] for _ in range(rows)]

        for row in range(rows):
            for col in range(columns):
                # Right-align the text
                self.cells[row][col].setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                layout.addWidget(self.cells[row][col], row, col)

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

        edit_action = menu.addAction("Edit")
        delete_action = menu.addAction("Delete")

        action = menu.exec_(self.mapToGlobal(pos))

        if action == edit_action:
            self.edit_table()
        elif action == delete_action:
            self.delete_table()

    def edit_table(self):
        rows, ok1 = QInputDialog.getInt(self, "Edit Rows", "Enter the number of rows:", self.rows, 1, 100, 1)
        columns, ok2 = QInputDialog.getInt(self, "Edit Columns", "Enter the number of columns:", self.columns, 1, 100, 1)

        if ok1 and ok2:
            self.update_table(rows, columns)

    def update_table(self, rows, columns):
        # Keep track of existing data
        existing_data = [[self.cells[row][col].text() for col in range(self.columns)] for row in range(self.rows)]

        self.rows = rows
        self.columns = columns

        # Clear existing cells
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                self.cells[row][col].deleteLater()

        # Create new cells
        self.cells = [[QLineEdit(self) for _ in range(columns)] for _ in range(rows)]

        layout = self.layout()
        for row in range(rows):
            for col in range(columns):
                # Set the text in the new cell
                if row < len(existing_data) and col < len(existing_data[row]):
                    self.cells[row][col].setText(existing_data[row][col])
                # Right-align the text
                self.cells[row][col].setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                layout.addWidget(self.cells[row][col], row, col)

    def delete_table(self):
        self.setParent(None)
        self.deleteLater()
