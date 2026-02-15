import random
from block import Block

class ConsensusEngine:
    def __init__(self, network, required_approvals=3):
        self.network = network
        self.required_approvals = required_approvals

    def propose_block(self, proposer_id, data):
        proposer = self.network.get_node(proposer_id)
        last_block = proposer.blockchain.get_latest_block()

        new_block = Block(
            index=len(proposer.blockchain.chain),
            data=data,
            previous_hash=last_block.hash
        )

        print(f"\n[PROPOSE] {proposer_id} proposes block {new_block.index}")
        approvals = 0

        for node in self.network.nodes:
            # Byzantine behavior: random lie
            if node.malicious:
                decision = random.choice([True, False])
                print(f"[{node.node_id}] Byzantine decision: {'APPROVE' if decision else 'REJECT'}")
            else:
                decision = node.verify_block(new_block)
                print(f"[{node.node_id}] Honest decision: {'APPROVE' if decision else 'REJECT'}")

            if decision:
                approvals += 1

        if approvals >= self.required_approvals:
            print(f"[COMMIT] Consensus reached with {approvals} approvals")
            for node in self.network.nodes:
                if not node.malicious:
                    node.blockchain.chain.append(new_block)
            return True
        else:
            print(f"[ABORT] Consensus failed ({approvals} approvals)")
            return False
