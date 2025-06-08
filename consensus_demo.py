import random

# Simulate Proof of Work
def pow_simulation():
    miners = [{"name": "MinerA", "power": random.randint(1, 100)},
              {"name": "MinerB", "power": random.randint(1, 100)}]
    winner = max(miners, key=lambda x: x["power"])
    print(f"[PoW] Selected: {winner['name']} with power {winner['power']}")

# Simulate Proof of Stake
def pos_simulation():
    stakers = [{"name": "StakerA", "stake": random.randint(1, 100)},
               {"name": "StakerB", "stake": random.randint(1, 100)}]
    winner = max(stakers, key=lambda x: x["stake"])
    print(f"[PoS] Selected: {winner['name']} with stake {winner['stake']}")

# Simulate Delegated Proof of Stake
def dpos_simulation():
    delegates = ["DelegateA", "DelegateB", "DelegateC"]
    votes = {d: random.randint(0, 10) for d in delegates}
    winner = max(votes, key=votes.get)
    print(f"[DPoS] Votes: {votes}")
    print(f"[DPoS] Selected: {winner} with {votes[winner]} votes")

# Run all
pow_simulation()
pos_simulation()
dpos_simulation()