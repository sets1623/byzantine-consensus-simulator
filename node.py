from blockchain import Blockchain

class Node:
    def __init__(self, node_id, malicious=False):
        self.node_id = node_id
        self.malicious = malicious
        self.blockchain = Blockchain()
        self.inbox = []

    def receive_message(self, message):
        self.inbox.append(message)

    def verify_block(self, block):
        # Malicious node always lies
        if self.malicious:
            return False

        # Honest node verifies hash
        expected_hash = block.calculate_hash()
        return block.hash == expected_hash

    def __repr__(self):
        status = "Malicious" if self.malicious else "Honest"
        return f"Node({self.node_id}, {status})"
