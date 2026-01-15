from fpdf import FPDF
import numpy as np
import matplotlib.pyplot as plt
import os

# ------------------ Setup folders ------------------
os.makedirs("graphs", exist_ok=True)
os.makedirs("report", exist_ok=True)

# ------------------ Ising Model Parameters ------------------
L = 20        # lattice size
J = 1         # interaction strength
kT = 2.0      # temperature
steps = 1000  # Monte Carlo steps

# Initialize lattice (+1 or -1 spins)
lattice = np.random.choice([-1, 1], size=(L, L))

# Function to calculate energy change for flipping a spin
def delta_E(lattice, i, j):
    left   = lattice[i, (j-1)%L]
    right  = lattice[i, (j+1)%L]
    up     = lattice[(i-1)%L, j]
    down   = lattice[(i+1)%L, j]
    return 2 * J * lattice[i,j] * (left + right + up + down)

# Monte Carlo Simulation (Metropolis)
for step in range(steps):
    i = np.random.randint(0, L)
    j = np.random.randint(0, L)
    dE = delta_E(lattice, i, j)
    if dE <= 0 or np.random.rand() < np.exp(-dE/kT):
        lattice[i,j] *= -1

# ------------------ Plot lattice ------------------
plt.figure(figsize=(6,6))
plt.imshow(lattice, cmap='coolwarm', interpolation='nearest')
plt.title(f"Ising Model Lattice (L={L}, T={kT})")
plt.colorbar(label='Spin')
plt.savefig("graphs/ising_lattice.png", dpi=150)
plt.close()

# ------------------ PDF Report ------------------
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Ising Model Simulation", ln=True, align="C")

# Method + Description
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 6,
f"""Objective:
Simulate a 2D Ising model lattice using Monte Carlo Metropolis algorithm.

Method:
- Lattice size = {L}x{L}
- Temperature T = {kT}
- Monte Carlo steps = {steps}
- Spins flip according to Metropolis criterion:
    - Flip accepted if energy decreases
    - Otherwise accepted with probability exp(-dE/kT)

Result:
- Final lattice configuration shown below.
""")

# Insert lattice plot
pdf.image("graphs/ising_lattice.png", x=20, w=160)
pdf.output("report/report_ising.pdf")

print("Phase 4 complete: Ising lattice graph + PDF generated successfully")