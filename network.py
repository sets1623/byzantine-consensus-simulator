class Network:
    def __init__(self, nodes):
        self.nodes = nodes

    def broadcast(self, message):
        for node in self.nodes:
            node.receive_message(message)

    def get_node(self, node_id):
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None
