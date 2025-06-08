import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return f"Block {self.index}:\n\tTimestamp: {self.timestamp}\n\tData: {self.data}\n\tPrevious Hash: {self.previous_hash}\n\tHash: {self.hash}\n"

# Create 3 linked blocks
block0 = Block(0, time.ctime(), "Genesis Block", "0")
block1 = Block(1, time.ctime(), "Block 1 Data", block0.hash)
block2 = Block(2, time.ctime(), "Block 2 Data", block1.hash)

# Display blocks
print(block0)
print(block1)
print(block2)

# Challenge: Tamper Block 1
block1.data = "Tampered Data"
block1.hash = block1.calculate_hash()

print("\nAfter tampering with Block 1:")
print(block1)
print("Block 2 now points to an invalid previous hash:", block2.previous_hash != block1.hash)