**Objective:** Demonstrate the application of Monte Carlo methods in computational physics through simulations, visualizations, and reports.

---

## **Project Overview**

This repository contains a series of Monte Carlo simulations designed to illustrate key concepts in computational physics. Each phase demonstrates an independent experiment, including the simulation code, graphical outputs, and a PDF report summarizing methods and results.

Monte Carlo methods provide a powerful framework for approximating solutions to problems that are difficult to solve analytically. These projects highlight skills in **Python programming, statistical modeling, data visualization, and scientific reporting**.

---

## **Phase 1: Monte Carlo π Estimation**

**Objective:** Estimate the value of π using random sampling within a unit square.  

**Method:**  
1. Generate 10,000 random points within a unit square.  
2. Count how many points fall inside the unit circle.  
3. Estimate π using the formula:  
   \[
   \pi \approx 4 \times \frac{\text{points inside circle}}{\text{total points}}
   \]

**Files:**  
- `code/pi_estimation.py` — Python script for the simulation.  
- `graphs/pi_plot.png` — Scatter plot showing points inside/outside the circle.  
- `report/report_pi.pdf` — PDF report with methodology, results, and plot.  

**Result:** Estimated π printed in the console and visualized in the plot.

---

## **Phase 2: 1D Random Walk**

**Objective:** Simulate the behavior of a particle performing a 1D random walk.  

**Method:**  
1. Simulate a single particle taking 1,000 steps, choosing ±1 randomly at each step.  
2. Repeat for 5,000 particles to analyze the distribution of final positions.  
3. Visualize a single trajectory and the histogram of final positions (Gaussian-like).  

**Files:**  
- `code/random_walk.py` — Simulation of random walks.  
- `graphs/random_walk_path.png` — Plot of a single trajectory.  
- `graphs/final_position_histogram.png` — Histogram of final positions.  
- `report/report_random_walk.pdf` — PDF report summarizing methodology, results, and graphs.  

**Result:** Demonstrates diffusion-like behavior and statistical distribution.

---

## **Phase 3: Monte Carlo Integration**

**Objective:** Estimate the integral of a function using random sampling.  

**Method:**  
1. Sample random points under the curve of a target function.  
2. Estimate the integral by calculating the fraction of points below the curve multiplied by the total area.  
3. Compare the estimated integral with the exact value.  

**Files:**  
- `code/monte_carlo_integration.py` — Python script for Monte Carlo integration.  
- `graphs/integration_plot.png` — Points plotted under the curve.  
- `report/report_integration.pdf` — PDF report showing method, plots, and comparison.  

**Result:** Demonstrates probabilistic estimation of integrals.

---

## **Phase 4: Ising Model Simulation (2D Lattice)**

**Objective:** Simulate the 2D Ising model to study spin interactions and phase transitions.  

**Method:**  
1. Create a 10x10 lattice of spins (+1 or -1).  
2. Simulate spin interactions using a Monte Carlo approach (Metropolis algorithm).  
3. Visualize lattice configurations and energy evolution.  

**Files:**  
- `code/ising_model.py` — Python simulation of the Ising lattice.  
- `graphs/lattice_heatmap.png` — Visualization of spin configuration.  
- `report/report_ising_model.pdf` — PDF report summarizing methodology, plots, and results.  

**Result:** Demonstrates emergence of ordered patterns and basic statistical mechanics principles.

---

## **Conclusion**

This portfolio demonstrates:  
- Proficiency in Monte Carlo methods and computational physics.  
- Ability to write Python code, generate data visualizations, and produce professional PDF reports.  
- Understanding of probabilistic modeling, statistical mechanics, numerical integration, and randomness in physical systems.  
- Organizational skills in structuring a clear and professional repository.
