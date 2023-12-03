# operation_nodes.py
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem


class OperationNode(QGraphicsEllipseItem):
    def __init__(self, operation, radius=20):
        super().__init__(-radius, -radius, 2 * radius, 2 * radius)
        self.operation = operation
        self.setFlag(QGraphicsEllipseItem.ItemIsMovable)
        self.setFlag(QGraphicsEllipseItem.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)
        self.text_item = QGraphicsTextItem(operation, parent=self)

    def mousePressEvent(self, event):
        print(f"Clicked on Operation Node: {self.operation}")
        super().mousePressEvent(event)
