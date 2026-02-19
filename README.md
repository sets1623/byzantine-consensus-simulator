# 🛡️ Byzantine Consensus Simulator

A simulation framework for analyzing **Byzantine Fault Tolerant (BFT) consensus algorithms** in distributed systems.  
This project models honest and malicious nodes, message passing, and consensus behavior under Byzantine failures.

---

## 📌 Overview

Distributed systems must continue functioning correctly even when some nodes fail or act maliciously.  
Such failures are known as **Byzantine faults**.

The **Byzantine Consensus Simulator** provides a controlled environment to:
- Study consensus behavior under Byzantine conditions
- Experiment with malicious node strategies
- Validate theoretical fault-tolerance limits
- Understand real-world distributed consensus challenges

Designed for **education, research, and experimentation**.

---

## ⚙️ Features

- Configurable number of nodes
- Honest and Byzantine node modeling
- Message-passing network simulation
- Consensus decision validation
- Fault tolerance threshold testing
- Deterministic and randomized simulations
- Modular and extensible architecture

---

## 🧠 Concepts Covered

- Byzantine Generals Problem
- Byzantine Fault Tolerance (BFT)
- Distributed consensus algorithms
- Malicious vs faulty node behavior
- Quorum-based agreement
- Message integrity and reliability

---

## 🏗️ Project Structure

```text
byzantine-consensus-simulator/
│
├── src/
│   ├── node.py          # Defines honest and Byzantine node behavior
│   ├── consensus.py    # Implements consensus logic and decision rules
│   └── network.py      # Simulates message passing between nodes
│
├── simulations/
│   └── test_cases.py   # Byzantine failure and attack scenarios
│
├── main.py             # Simulation entry point
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
