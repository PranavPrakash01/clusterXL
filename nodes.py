# THE NODE CLASS

class Node:
    def __init__(self, node_id, data=None):
        self.node_id = node_id
        self.data = data if data is not None else {}  # Store node-specific data
        self.connections = []  # List to store connected nodes

    def connect(self, other_node):
        if other_node not in self.connections:
            self.connections.append(other_node)

    def disconnect(self, other_node):
        if other_node in self.connections:
            self.connections.remove(other_node)

# THE NODE GRAPH

class NodeGraph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)

    def connect_nodes(self, node1, node2):
        node1.connect(node2)
        node2.connect(node1)

    def disconnect_nodes(self, node1, node2):
        node1.disconnect(node2)
        node2.disconnect(node1)
