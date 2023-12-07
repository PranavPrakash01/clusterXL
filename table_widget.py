# table_widget.py
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QMenu, QInputDialog
from PyQt5.QtCore import Qt, QPoint

class TableWidget(QWidget):
    def __init__(self, rows, columns):
        super().__init__()

        self.is_dragging = False
        self.offset = QPoint()

        self.cell_width = 75  
        self.cell_height = 25

        # Keep track of cell data
        self.cell_data = [[None for _ in range(columns)] for _ in range(rows)]

        self.layout = QGridLayout(self)
        self.cells = []

        # Create the initial table structure
        self.create_table(rows, columns)
        

    def create_table(self, rows, columns):
        self.cells = [[QLineEdit(self) for _ in range(columns)] for _ in range(rows)]

        self.layout.setSpacing(0)  # Set spacing to 0 to reduce the distance between cells
        for row in range(rows):
            for col in range(columns):
                # Set the text in the new cell
                if row < len(self.cell_data) and col < len(self.cell_data[row]):
                    self.cells[row][col].setText(self.cell_data[row][col])

                # Right-align the text
                self.cells[row][col].setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.layout.addWidget(self.cells[row][col], row, col)

                self.cells[row][col].setFixedSize(self.cell_width, self.cell_height)

        # Resize the widget
        self.adjustSize()

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
        current_rows, current_columns = len(self.cells), len(self.cells[0])

        rows_input, ok1 = QInputDialog.getInt(self, "Edit Rows", "Enter the number of rows:", value=current_rows, min=1, max=100, step=1)
        columns_input, ok2 = QInputDialog.getInt(self, "Edit Columns", "Enter the number of columns:", value=current_columns, min=1, max=100, step=1)

        if ok1 and ok2:
            self.update_table(rows_input, columns_input)

    def update_table(self, rows, columns):
        # Keep track of existing data
        existing_data = [[self.cells[row][col].text() for col in range(len(self.cells[row]))] for row in range(len(self.cells))]

        # Clear existing cells
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                widget = self.layout.itemAtPosition(row, col).widget()
                self.layout.removeWidget(widget)
                widget.deleteLater()

        # Create new cells
        self.cells = [[QLineEdit(self) for _ in range(columns)] for _ in range(rows)]

        self.layout.setSpacing(0)  # Set spacing to 0 to reduce the distance between cells
        for row in range(rows):
            for col in range(columns):
                # Set the text in the new cell
                if row < len(existing_data) and col < len(existing_data[row]):
                    self.cells[row][col].setText(existing_data[row][col])
                # Right-align the text
                self.cells[row][col].setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.layout.addWidget(self.cells[row][col], row, col)

                self.cells[row][col].setFixedSize(self.cell_width, self.cell_height)

        # Resize the widget
        self.adjustSize()

    def delete_table(self):
        self.setParent(None)
        self.deleteLater()
