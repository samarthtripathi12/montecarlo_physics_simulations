from fpdf import FPDF
import os

# Ensure report folder exists
report_folder = "../report"
os.makedirs(report_folder, exist_ok=True)

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Monte Carlo Random Walk Simulation", ln=1, align='C')

pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 6,
"""
Objective:
Visualize 1D random walks and final position distribution using Monte Carlo simulation.

Method:
- Generate 1000 steps for a single walk
- Plot cumulative position (path)
- Generate 5000 walks, record final positions
- Plot histogram of final positions

Results:
Graphs show single walk path and final position histogram (Gaussian distribution).

Conclusion:
Random walks converge to a Gaussian distribution of final positions (Central Limit Theorem).
"""
)

# Insert graphs
pdf.image("../graphs/random_walk_path.png", x=20, w=160)
pdf.ln(10)
pdf.image("../graphs/final_position_histogram.png", x=20, w=160)

# Save PDF
pdf.output(os.path.join(report_folder, "report_random_walk.pdf"))
print("Phase 2 PDF generated successfully!")
