# operation_nodes.py
from PyQt5.QtWidgets import QMenu, QAction

def create_operation_menu(main_window):
    # Create a menu
    menu = QMenu(main_window)

    # Create actions for single input operations
    single_input_menu = menu.addAction("Single Input Operations")

    # Create actions for double input operations
    double_input_menu = menu.addAction("Double Input Operations")

    # Create actions for multi input operations
    multi_input_menu = menu.addAction("Multi Input Operations")

    # Show the menu at the cursor position
    action = menu.exec_(main_window.cursor().pos())

    # Add logic here to handle the selected action
    if action:
        print(f"Selected operation: {action.text()}")
