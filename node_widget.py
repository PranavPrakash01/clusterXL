# node_widget.py
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsSceneMouseEvent


class NodeWidget(QGraphicsRectItem):
    def __init__(self, node, width=50, height=30):
        super().__init__(-width/2, -height/2, width, height)
        self.node = node
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setAcceptHoverEvents(True)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent):
        print(f"Clicked on Node {self.node.node_id}")
        super().mousePressEvent(event)