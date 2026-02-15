import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + self.previous_hash
        )
        return hashlib.sha256(content.encode()).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash[:10]}...)"
