# table_widget.py
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QMenu, QLabel, QVBoxLayout,QInputDialog, QHBoxLayout
from PyQt5.QtCore import Qt, QPoint
from Single_Input_Operations.connection_point import ConnectionPoint

class TableWidget(QWidget):
    def __init__(self, table_id, rows, columns):
        super().__init__()

        self.is_dragging = False
        self.offset = QPoint()
        self.table_id = table_id

        self.cell_width = 75
        self.cell_height = 25
        self.connection_point_radius = 5

        # Keep track of cell data
        self.cell_data = [[None for _ in range(columns)] for _ in range(rows)]

        # Main vertical layout for the table
        main_layout = QVBoxLayout(self)

        # Title label
        title_label = QLabel(f"Title {self.table_id}")
        main_layout.addWidget(title_label)

        # Grid layout for cells
        self.layout = QGridLayout()
        self.cells = []

        # Create the initial table structure
        self.create_table(rows, columns)

        # Add the grid layout to the main layout
        main_layout.addLayout(self.layout)

        # Create and add the ConnectionPoints below the grid
        self.create_and_position_connection_points(columns)
        self.add_connection_points_to_layout(main_layout)

    def create_and_position_connection_points(self, columns):
        self.connection_points = [ConnectionPoint(self, node_type="Table", column=col + 1) for col in range(columns)]

    def add_connection_points_to_layout(self, layout):
        # Create a horizontal layout for connection points
        connection_points_layout = QHBoxLayout()

        # Add connection points to the layout
        for connection_point in self.connection_points:
            connection_points_layout.addWidget(connection_point)

        # Add the connection points layout to the main layout
        layout.addLayout(connection_points_layout)

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