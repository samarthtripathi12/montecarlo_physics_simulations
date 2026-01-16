# Monte Carlo Physics Simulations

A curated computational physics portfolio demonstrating **Monte Carlo methods** across probability, stochastic processes, numerical integration, and statistical mechanics. This repository emphasizes **clear results**, **visual intuition (plots + GIFs)**, and **research-style documentation (PDFs)**.

> **Why this matters:** Monte Carlo techniques power modern physics, quantitative finance, materials science, and AI. Each phase here is designed to scale conceptually—from simple randomness to emergent collective behavior.

---

## Phase 1: Monte Carlo π Estimation

**Objective**
Estimate the value of π using random sampling and geometric probability.

### Method

* Generate **10,000 random points** uniformly inside a unit square.
* Count points that fall inside the unit circle.
* Estimate π using:

[\pi \approx 4 \times \frac{N_{\text{inside circle}}}{N_{\text{total}}}]

### Results

* **Estimated π ≈ 3.1416**
* Convergence improves with increased sampling.

**Scatter Plot**

![Pi Estimation](MonteCarlo_Phase1/pi_plot.png)

**PDF Report**
[Download PDF](MonteCarlo_Phase1/report_pi.pdf)

**Insight**
This phase establishes statistical convergence and variance—foundations required for all later simulations.

---

## Phase 2: 1D Random Walk (Stochastic Dynamics)

**Objective**
Model diffusion-like behavior using a one-dimensional random walk.

### Method

* Simulate a single particle taking **1,000 steps** with equal probability of (+1, -1).
* Repeat for **5,000 independent particles**.
* Analyze trajectory evolution and final position distribution.

### Results

**Single Particle Trajectory (Static)**

![Random Walk Path](MonteCarlo_Phase2_RandomWalk/graphs/random_walk_path.png)

**Final Position Distribution**
(Approaches a Gaussian as predicted by the Central Limit Theorem)

![Final Position Histogram](MonteCarlo_Phase2_RandomWalk/graphs/final_position_histogram.png)

**Dynamic Evolution (GIF)**
*Time evolution of the random walk trajectory*

![Random Walk GIF](MonteCarlo_Phase2_RandomWalk/graphs/random_walk.gif)

**PDF Report**
[Download PDF](MonteCarlo_Phase2_RandomWalk/report/report_random_walk.pdf)

**Why this is bigger than it looks**
This same model underlies **Brownian motion**, **stock price diffusion**, **heat transport**, and **noise in neural systems**.

---

## Phase 3: Monte Carlo Integration (Numerical Methods)

**Objective**
Estimate definite integrals using random sampling and compare with analytical solutions.

### Method

* Uniformly sample random points under a target function.
* Estimate the integral via area-weighted probability.
* Compare Monte Carlo estimate with the exact value.

### Results

**Monte Carlo Integration Visualization**

![Monte Carlo Integration](Phase3_MonteCarlo_Integration/graphs/integration_plot.png)

**PDF Report**
[Download PDF](Phase3_MonteCarlo_Integration/report_integration.pdf)

**Insight**
Monte Carlo integration scales efficiently to **high-dimensional integrals**, where classical numerical methods fail—critical in quantum mechanics and Bayesian inference.

---

## Phase 4: 2D Ising Model (Statistical Mechanics)

**Objective**
Simulate emergent collective behavior from simple local spin interactions.

### Method

* Initialize a **10×10 lattice** of spins (±1).
* Apply the **Metropolis algorithm** to evolve the system.
* Observe spin alignment and domain formation.

### Results

**Static Spin Configuration**

![Ising Model Lattice](Phase4_IsingModel/graphs/ising_lattice.png)

**Thermal Evolution (GIF)**
*Spin domain formation over Monte Carlo steps*

![Ising Model GIF](Phase4_IsingModel/graphs/ising_evolution.gif)

**PDF Report**
[Download PDF](Phase4_IsingModel/report_ising.pdf)

**Why this matters**
The Ising model connects directly to **phase transitions**, **magnetism**, **neural networks**, and even **social dynamics**—simple rules generating complex order.

---

## Conclusion

This portfolio demonstrates:

* Strong command of **Monte Carlo techniques**
* Ability to connect simulations to **real physical phenomena**
* Clean visualization using **plots, heatmaps, and GIFs**
* Research-level documentation via structured **PDF reports**

> From randomness to emergence, this project shows not just implementation—but **thinking like a physicist**.

---

## Folder Structure

```
MonteCarlo_Physics_Simulations/
│
├── MonteCarlo_Phase1/
│   ├── pi_plot.png
│   └── report_pi.pdf
│
├── MonteCarlo_Phase2_RandomWalk/
│   ├── graphs/
│   │   ├── random_walk_path.png
│   │   └── final_position_histogram.png
│   ├── gifs/
│   │   └── random_walk_evolution.gif
│   └── report/
│       └── report_random_walk.pdf
│
├── Phase3_MonteCarlo_Integration/
│   ├── graphs/
│   │   └── integration_plot.png
│   └── report_integration.pdf
│
├── Phase4_IsingModel/
│   ├── graphs/
│   │   └── ising_lattice.png
│   ├── gifs/
│   │   └── ising_evolution.gif
│   └── report_ising.pdf
│
└── README.md
```
