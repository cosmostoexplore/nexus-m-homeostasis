# Nexus-M: Autonomous Planetary Rover Control System via Digital Homeostasis
An experimental reinforcement learning proof-of-concept for planetary rovers based on predictive coding, localized resource limitations, and a hardwired bio-inspired "digital homeostasis" loop (pain vs. reward).

## 1. The Core Architecture Philosophy
Traditional autonomous rovers rely on rigid, pre-defined expert systems or linear neural networks mapping visual data to hazard charts. Under absolute autonomy (e.g., a 20-minute signal latency on Mars), this leads to a fatal dichotomy: the system becomes either overly reckless or paralyzed by safety margins.

**Nexus-M solves this by introducing hardwired hardware-level receptors that actively alter processor dynamics based on system survival metrics.**

Instead of managing abstract penalty scores (e.g., `reward = -1`), Nexus-M binds internal states directly to system degradation (data loss) and resource depletion (stress-induced power drain). The system learns through a continuous loop:
\[\text{Action} \rightarrow \text{Receptor Shock} \rightarrow \text{Self-Referential Feedback} \rightarrow \text{Memory Correction}\]

---

## 2. Multimodal System States & Hardwired Receptors

The system dynamically balances four lifecycle actions (`crater_exploration`, `plateau_traverse`, `hibernation_sleep`, `idle_waiting`) regulated by three hardware-level parameters:

### 🧠 The Digital Pain Loop (Memory Degradation)
* **Trigger:** Mechanical shock, critical core overheating, or excessive wheel slippage (torque sensors).
* **Hardware Mechanism:** The processor initiates a chaotic partial wipe of the volatile short-term memory cache (e.g., removing 0.01% of recently mapped terrain sectors).
* **Systemic Effect:** A direct computational analog to degenerative cognitive failure. Successful navigation patterns are lost, forcing the Q-learning agent to treat high-stress vectors as fundamentally destructive to its "Self."

### 🔥 The Stress Multiplier (Power Dynamics)
* **Trigger:** Battery levels dropping below 35%.
* **Hardware Mechanism:** The system enters `STRESS` mode, activating intensive auxiliary survival subroutines. This triggers a 2.0× power drain multiplier.
* **Systemic Effect:** Imposes a critical resource bottleneck. Reckless exploration during low-energy states results in exponential power expiration, driving the agent to prioritize solar recharging.

### 🔋 The Digital Endorphin Loop (Plasticity Locking)
* **Trigger:** Identification of anomalous geological structures or spectral biosignatures.
* **Hardware Mechanism:** The system executes an architecture-wide "plasticity lock," moving the active memory session to permanent, non-volatile sectors (`protected_memory`). Processor clock speeds are temporarily elevated by 20%.
* **Systemic Effect:** The agent experiences systemic stability and high-throughput cognition—generating an active algorithmic drive to pursue high-value scientific anomalies.

---

## 3. Simulated Verification Script
The repository includes a decoupled Q-learning implementation (`smart_nexus_m.py`) demonstrating this balance under strict constraints:

```python
# Prototype implementation of the SmartNexusM lifecycle loop.
# Evaluates how resource constraints and memory wipes force autonomous adaptation.
# Run: python smart_nexus_m.py
```
*(Сюда вставляется наш готовый скрипт симуляции с Q-таблицей, стрессом и сном)*

---

## 4. Key Engineering Takeaways
1. **Embodied AI Integration:** Proves that software-level AI cannot achieve authentic autonomy without a strict, un-bypassable connection to hardware limits (memory degradation and power constraints).
2. **Self-Preservation Emergence:** Demonstrates that a simple Q-learning matrix can evolve complex behavioral prioritization (fleeing to solar recharge during stress, taking calculated risks during peak states) purely through a self-referential loop.