# main.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from nodes import Node, NodeGraph
from operation_nodes import create_operation_menu
from add_table_dialog import AddTableDialog
from table_widget import TableWidget

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

        # Add the ribbon layout to the main layout
        layout.addLayout(ribbon_layout)

        # Add the QGraphicsView to the main layout
        layout.addWidget(self.view)

        # Create table nodes
        self.table_nodes = []

        # Create operation nodes
        self.operation_nodes = []

        # Create a graph instance
        self.graph = NodeGraph()

        # Show the main window
        self.showMaximized()

    def show_add_table_dialog(self):
        dialog = AddTableDialog(self)
        if dialog.exec_():
            # Get the values entered in the dialog
            rows = int(dialog.input_row.text())
            columns = int(dialog.input_column.text())

            # Create a new table node with specified rows and columns
            table_node = Node(node_id=len(self.table_nodes) + 1, data={"type": "Table", "rows": rows, "columns": columns})
            self.table_nodes.append(table_node)

            # Add table node to the graph
            self.graph.add_node(table_node)

            # Create a TableWidget and add it to the scene
            table_widget = TableWidget(rows, columns)
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
