import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash=''):
        self.index = index
        self.timestamp = time.ctime()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        text = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(text.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"Mining block with difficulty {'0' * difficulty}...")
        start_time = time.time()
        attempts = 0
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1
        end_time = time.time()
        print(f"Block mined! Hash: {self.hash}")
        print(f"Attempts: {attempts}, Time taken: {round(end_time - start_time, 4)} seconds\n")

# Simulate mining
difficulty = 4
block = Block(0, "Mining Simulation")
block.mine_block(difficulty)