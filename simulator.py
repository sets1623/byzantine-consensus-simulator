from node import Node
from network import Network
from consensus import ConsensusEngine

nodes = [
    Node("Node_1"),
    Node("Node_2"),
    Node("Node_3"),
    Node("Node_4", malicious=True)
]

network = Network(nodes)
consensus = ConsensusEngine(network)

print("\n=== Advanced Byzantine Consensus Simulation ===")

transactions = [
    {"sender": "Alice", "receiver": "Bob", "amount": 100},
    {"sender": "Bob", "receiver": "Charlie", "amount": 50},
    {"sender": "Charlie", "receiver": "Dave", "amount": 25},
]

success = 0

for i, tx in enumerate(transactions, start=1):
    print(f"\n--- ROUND {i} ---")
    if consensus.propose_block("Node_1", tx):
        success += 1

print(f"\n=== SUMMARY ===")
print(f"Successful commits: {success}/{len(transactions)}")

print("\n=== FINAL BLOCKCHAIN STATE (Honest Nodes) ===")
for node in nodes:
    if not node.malicious:
        print(f"\n{node}")
        for block in node.blockchain.chain:
            print(block)
