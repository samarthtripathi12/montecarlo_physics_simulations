from fpdf import FPDF
import numpy as np
import matplotlib.pyplot as plt
import os

# Create folders if not exist
os.makedirs("../graphs", exist_ok=True)
os.makedirs("../report", exist_ok=True)

# ---------- Parameters ----------
num_steps = 1000
num_walks = 5000

# ---------- Single Random Walk ----------
steps = np.random.choice([-1, 1], size=num_steps)
position = np.cumsum(steps)

plt.figure(figsize=(8,4))
plt.plot(position)
plt.xlabel("Step")
plt.ylabel("Position")
plt.title("1D Random Walk (Single Path)")
plt.grid(True)
plt.savefig("../graphs/random_walk_path.png", dpi=150)
plt.close()

# ---------- Many Random Walks ----------
final_positions = []
for _ in range(num_walks):
    steps = np.random.choice([-1, 1], size=num_steps)
    final_positions.append(np.sum(steps))

plt.figure(figsize=(6,4))
plt.hist(final_positions, bins=50, density=True)
plt.xlabel("Final Position")
plt.ylabel("Probability Density")
plt.title("Final Position Distribution (Gaussian)")
plt.grid(True)
plt.savefig("../graphs/final_position_histogram.png", dpi=150)
plt.close()

# ---------- Create PDF ----------
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0,10,"Monte Carlo Random Walk Simulation", ln=1, align='C')
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0,6,
"""
Objective:
Visualize 1D random walks and their final position distribution.

Method:
- Single random walk: 1000 steps
- Many walks: 5000 trials

Results:
- Single path plot
- Histogram shows Gaussian distribution
"""
)
pdf.image("../graphs/random_walk_path.png", x=20, w=160)
pdf.ln(5)
pdf.image("../graphs/final_position_histogram.png", x=20, w=160)
pdf.output("../report/report_random_walk.pdf")

print("Phase 2 complete: PDF generated")
