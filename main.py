# main.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt
from nodes import Node, NodeGraph
from node_widget import NodeWidget
from operation_nodes import OperationNode

def main():
    # Initialize the application
    app = QApplication([])

    # Create the main window
    window = QMainWindow()
    window.setWindowTitle("Node-based Spreadsheet")
    window.setGeometry(100, 100, 800, 600)

    # Create a QGraphicsScene
    scene = QGraphicsScene()
    scene.setSceneRect(-400, -300, 800, 600)

    # Create a QGraphicsView
    view = QGraphicsView(scene)
    view.setAlignment(Qt.AlignLeft | Qt.AlignTop)

    # Set up the main window layout
    layout = QMainWindow()
    layout.setCentralWidget(view)

    # Create table nodes
    table_node1 = Node(node_id=1, data={"type": "Table"})
    table_node2 = Node(node_id=2, data={"type": "Table"})

    # Create operation nodes
    addition_node = OperationNode(operation="Addition")
    subtraction_node = OperationNode(operation="Subtraction")

    # Add nodes to the graph
    graph = NodeGraph()
    graph.add_node(table_node1)
    graph.add_node(table_node2)

    # Connect nodes
    graph.connect_nodes(table_node1, table_node2)

    # Add table nodes to the scene
    node_widget1 = NodeWidget(table_node1, width=50, height=30)
    node_widget2 = NodeWidget(table_node2, width=50, height=30)
    scene.addItem(node_widget1)
    scene.addItem(node_widget2)

    # Add operation nodes to the scene
    scene.addItem(addition_node)
    scene.addItem(subtraction_node)

    # Position nodes in the scene
    node_widget1.setPos(-200, 0)
    node_widget2.setPos(200, 0)
    addition_node.setPos(0, -200)
    subtraction_node.setPos(0, 200)

    # Show the main window
    window.setCentralWidget(layout)
    window.show()

    # Start the application event loop
    app.exec_()

if __name__ == "__main__":
    main()
    