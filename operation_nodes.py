# operations.py
from PyQt5.QtWidgets import QMenu, QAction, QGraphicsProxyWidget
from Single_Input_Operations.average_node import AverageNode

def create_operation_menu(main_window):
    # Create a menu
    menu = QMenu(main_window)

    # Create actions for single input operations
    single_input_menu = menu.addMenu("Single Input Operations")
    average_action = single_input_menu.addAction("Average")
    average_action.triggered.connect(lambda: add_average_node(main_window))

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

    # Create a proxy widget for AverageNode
    proxy_widget = QGraphicsProxyWidget()
    proxy_widget.setWidget(average_node)

    main_window.scene.addItem(proxy_widget)