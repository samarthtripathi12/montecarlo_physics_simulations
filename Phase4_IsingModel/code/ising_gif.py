import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
L = 20
steps = 200
J = 1.0
T = 2.0

# Initialize lattice
lattice = np.random.choice([-1, 1], size=(L, L))

def energy(i, j):
    s = lattice[i, j]
    neighbors = lattice[(i+1)%L, j] + lattice[(i-1)%L, j] + \
                lattice[i, (j+1)%L] + lattice[i, (j-1)%L]
    return 2 * J * s * neighbors

fig, ax = plt.subplots()
im = ax.imshow(lattice, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_title("Ising Model Evolution")

def update(frame):
    for _ in range(L * L):
        i = np.random.randint(0, L)
        j = np.random.randint(0, L)
        dE = energy(i, j)
        if dE <= 0 or np.random.rand() < np.exp(-dE / T):
            lattice[i, j] *= -1
    im.set_array(lattice)
    return [im]

ani = animation.FuncAnimation(
    fig, update, frames=steps, interval=50
)

ani.save("../graphs/ising_evolution.gif", writer="pillow")
plt.close()

print("Phase 4 GIF generated: ising_evolution.gif")

