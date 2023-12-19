# main.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from nodes import Node, NodeGraph
from operation_nodes import create_operation_menu
from add_table_dialog import AddTableDialog
from table_widget import TableWidget
from PyQt5.QtGui import QPen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main window
        self.setWindowTitle("Node-based Spreadsheet")

        # Create a central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create a ribbon layout
        ribbon_layout = QHBoxLayout()

        # Create a QGraphicsScene
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(-400, -300, 800, 600)

        # Create a QGraphicsView
        self.view = QGraphicsView(self.scene)
        self.view.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # Create buttons and add them to the ribbon
        self.addButton = QPushButton("Add Table", self)
        self.addButton.clicked.connect(self.show_add_table_dialog)
        ribbon_layout.addWidget(self.addButton)

        self.addOperationButton = QPushButton("Add Operation", self)
        self.addOperationButton.clicked.connect(self.add_operation_node)
        ribbon_layout.addWidget(self.addOperationButton)

        #------------------------------------------------------------------
        # Add the new button for testing lines
        self.testLinesButton = QPushButton("Test Lines", self)
        self.testLinesButton.clicked.connect(self.start_test_lines)
        ribbon_layout.addWidget(self.testLinesButton)

        # Variable to track whether "Test Lines" mode is active
        self.test_lines_mode = False

        # Variables to store the starting and ending points for the line
        self.start_point = None
        self.end_point = None
        #------------------------------------------------------------------

        # Add the ribbon layout to the main layout
        layout.addLayout(ribbon_layout)

        # Add the QGraphicsView to the main layout
        layout.addWidget(self.view)

        # Create table nodes
        self.table_nodes = []
        self.table_id_counter = 0  # Counter to keep track of table IDs

        # Create operation nodes
        self.operation_nodes = []

        # Create a graph instance
        self.graph = NodeGraph()

        # Show the main window
        self.showMaximized()

    #------------------------------------------------------------------
    # Define the function to be executed when the "Test Lines" button is clicked
    def start_test_lines(self):
        # Enable the test lines mode only if it's not already active
        if not self.test_lines_mode:
            self.test_lines_mode = True
            print(self.test_lines_mode)

            # Clear any previous points
            self.start_point = None
            self.end_point = None

            # Connect the scene's mouse press event to handle clicking points
            self.scene.mousePressEvent = self.handle_test_lines_mouse_press

    # Define the function to handle mouse press events during "Test Lines" mode
    def handle_test_lines_mouse_press(self, event):
        if self.test_lines_mode:
            # Get the position of the mouse click
            click_position = event.scenePos()

            # If start_point is None, set it to the current click position
            # If start_point is already set, set end_point and draw the line
            if self.start_point is None:
                self.start_point = click_position
            else:
                self.end_point = click_position

                # Draw a line between start_point and end_point
                line_item = self.scene.addLine(self.start_point.x(), self.start_point.y(),
                                               self.end_point.x(), self.end_point.y())

                # Set the line color and thickness (red, 2 pixels)
                line_item.setPen(QPen(Qt.red, 2))

                # Reset points for the next line
                self.start_point = None
                self.end_point = None

                # Disable test lines mode after drawing a line
                self.test_lines_mode = False

                # Disconnect the custom mouse press event, revert to the default behavior
                self.scene.mousePressEvent = None

    #------------------------------------------------------------------
        
    def show_add_table_dialog(self):
        dialog = AddTableDialog(self)
        if dialog.exec_():
            # Get the values entered in the dialog
            rows = int(dialog.input_row.text())
            columns = int(dialog.input_column.text())

            # Increment the table ID counter
            self.table_id_counter += 1

            # Create a new table node with specified rows, columns, and ID
            table_node = Node(node_id=len(self.table_nodes) + 1, data={"type": "Table", "rows": rows, "columns": columns, "id": self.table_id_counter})
            self.table_nodes.append(table_node)

            # Add table node to the graph
            self.graph.add_node(table_node)

            # Create a TableWidget with ID and add it to the scene
            table_widget = TableWidget(table_id=self.table_id_counter, rows=rows, columns=columns)
            self.scene.addWidget(table_widget)
            
    def add_operation_node(self):
        create_operation_menu(self)


def main():
    # Initialize the application
    app = QApplication([])

    # Create the main window
    main_window = MainWindow()

    # Start the application event loop
    app.exec_()

if __name__ == "__main__":
    main()
