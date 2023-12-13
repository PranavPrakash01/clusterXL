# operation_nodes.py
from PyQt5.QtWidgets import QMenu, QAction
from Single_Input_Operations.single_sum_node import SingleSumNode
from Single_Input_Operations.average_node import AverageNode
from nodes import Node

def create_operation_menu(main_window):
    # Create a menu
    menu = QMenu(main_window)

    # Create actions for single input operations
    single_input_menu = menu.addMenu("Single Input Operations")
    average_action = single_input_menu.addAction("Average")
    sum_action = single_input_menu.addAction("Sum")

    average_action.triggered.connect(lambda: add_average_node(main_window))
    sum_action.triggered.connect(lambda: add_sum_node(main_window))

    # Create actions for double input operations
    double_input_menu = menu.addMenu("Double Input Operations")
    # Add your double input actions here (e.g., RSum, RProduct, RDifference)

    # Create actions for multi input operations
    multi_input_menu = menu.addMenu("Multi Input Operations")
    # Add your multi input actions here (e.g., RSum, RProduct, RDifference)

    # ... (add more actions as needed)

    # Show the menu at the cursor position
    menu.exec_(main_window.cursor().pos())

def add_average_node(main_window):
    average_node = AverageNode()

    # Add average node to the scene
    main_window.scene.addWidget(average_node)

    # Add average node to the graph
    average_node_data = {"type": "AverageNode"}  # You might want to add more data
    average_node_graph = Node(node_id=len(main_window.graph.nodes) + 1, data=average_node_data)
    main_window.graph.add_node(average_node_graph)

def add_sum_node(main_window):
    sum_node = SingleSumNode()

    # Add sum node to the scene
    main_window.scene.addWidget(sum_node)

    # Add sum node to the graph
    sum_node_data = {"type": "SingleSumNode"}  # You might want to add more data
    sum_node_graph = Node(node_id=len(main_window.graph.nodes) + 1, data=sum_node_data)
    main_window.graph.add_node(sum_node_graph)