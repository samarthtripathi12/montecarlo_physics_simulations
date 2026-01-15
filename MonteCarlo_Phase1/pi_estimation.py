import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF

# Number of random points
N = 10000

# Generate random points in unit square
x = np.random.rand(N)
y = np.random.rand(N)

# Check points inside unit circle
inside = x**2 + y**2 <= 1
pi_estimate = 4 * np.sum(inside) / N

print("Estimated pi value:", pi_estimate)

# Plot the points
plt.figure(figsize=(6, 6))
plt.scatter(x[inside], y[inside], s=1, label="Inside Circle")
plt.scatter(x[~inside], y[~inside], s=1, label="Outside Circle")
circle = plt.Circle((0, 0), 1, fill=False)
plt.gca().add_artist(circle)
plt.axis("equal")
plt.title("Monte Carlo Estimation of Pi (N = {})".format(N))
plt.legend()
plt.savefig("pi_plot.png", dpi=150)
plt.close()

# Create PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Monte Carlo Simulation for Pi Estimation", ln=True, align="C")

pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 8,
    "Objective:\n"
    "Estimate the value of pi using Monte Carlo simulation.\n\n"
    "Method:\n"
    "- Generate random points inside a unit square\n"
    "- Count how many fall inside the unit circle\n"
    "- Estimate pi using probability\n\n"
    "Result:\n"
    "Estimated pi value = {:.6f}".format(pi_estimate)
)

pdf.image("pi_plot.png", x=30, w=150)
pdf.output("report_pi.pdf")

print("Phase 1 complete: pi_plot.png and report_pi.pdf created")