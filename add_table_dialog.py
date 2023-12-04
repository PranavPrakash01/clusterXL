# add_table_dialog.py
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class AddTableDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Table")
        self.setGeometry(100, 100, 300, 150)

        self.label_row = QLabel("Rows:", self)
        self.input_row = QLineEdit(self)

        self.label_column = QLabel("Columns:", self)
        self.input_column = QLineEdit(self)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)

        layout = QVBoxLayout(self)
        layout.addWidget(self.label_row)
        layout.addWidget(self.input_row)
        layout.addWidget(self.label_column)
        layout.addWidget(self.input_column)
        layout.addWidget(self.ok_button)
