from fpdf import FPDF
import numpy as np
import matplotlib.pyplot as plt
import os

# ------------------ Setup folders ------------------
os.makedirs("graphs", exist_ok=True)
os.makedirs("report", exist_ok=True)

# ------------------ Monte Carlo Integration ------------------
def f(x):
    return np.sin(x)

a, b = 0, np.pi
N = 10000

# Generate random points
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, 1, N)

# Count points under the curve
under_curve = y_rand < f(x_rand)
integral_estimate = (b - a) * np.sum(under_curve) / N

print("Estimated integral of sin(x) from 0 to pi:", round(integral_estimate, 6))

# ------------------ Plot ------------------
plt.figure(figsize=(6,4))
x_plot = np.linspace(a, b, 500)
plt.plot(x_plot, f(x_plot), 'b', label='sin(x)')
plt.scatter(x_rand[under_curve], y_rand[under_curve], color='green', s=1, label='Under curve')
plt.scatter(x_rand[~under_curve], y_rand[~under_curve], color='red', s=1, label='Above curve')
plt.title(f"Monte Carlo Integration (Estimate ≈ {round(integral_estimate,4)})")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.savefig("graphs/integration_plot.png", dpi=150)
plt.close()

# ------------------ PDF ------------------
pdf = FPDF()
pdf.add_page()

# Safe font
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Monte Carlo Integration Simulation", ln=True, align="C")

pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 6,
"Objective:\n"
"Estimate the integral of sin(x) from 0 to pi using Monte Carlo simulation.\n\n"
"Method:\n"
"- Generate {} random points in rectangle [0, pi] x [0,1]\n"
"- Count points under the curve\n"
"- Estimate integral = area * (points under curve / total points)\n\n"
"Result:\n"
"Estimated integral = {:.6f}".format(N, integral_estimate)
)

# Add plot
pdf.image("graphs/integration_plot.png", x=20, w=160)
pdf.output("report/report_integration.pdf")

print("Phase 3 complete: PDF generated successfully")