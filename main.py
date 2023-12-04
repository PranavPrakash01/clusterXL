# main.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QPushButton, QVBoxLayout, QWidget, QLineEdit
from PyQt5.QtCore import Qt
from nodes import Node, NodeGraph
from node_widget import NodeWidget
from operation_nodes import OperationNode
from add_table_dialog import AddTableDialog
from table_widget import TableWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the main window
        self.setWindowTitle("Node-based Spreadsheet")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create a QGraphicsScene
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(-400, -300, 800, 600)

        # Create a QGraphicsView
        self.view = QGraphicsView(self.scene)
        self.view.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(self.view)

        # Create table nodes
        self.table_nodes = []

        # Create operation nodes
        self.operation_nodes = []

        # Create buttons
        self.addButton = QPushButton("Add Table", self)
        self.addButton.clicked.connect(self.show_add_table_dialog)
        layout.addWidget(self.addButton)

        self.addOperationButton = QPushButton("Add Operation", self)
        self.addOperationButton.clicked.connect(self.add_operation_node)
        layout.addWidget(self.addOperationButton)

        # Create a graph instance
        self.graph = NodeGraph()

        # Show the main window
        self.show()

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

            # Position the table in the scene
            table_widget.setGeometry(0, 0, columns * 100, rows * 30)

    def add_operation_node(self):
        # Create a new operation node
        operation_node = OperationNode(operation="Addition")
        self.operation_nodes.append(operation_node)

        # Add operation node to the scene
        self.scene.addItem(operation_node)

        # Position the node in the scene
        operation_node.setPos(0, 0)

def main():
    # Initialize the application
    app = QApplication([])

    # Create the main window
    main_window = MainWindow()

    # Start the application event loop
    app.exec_()

if __name__ == "__main__":
    main()
