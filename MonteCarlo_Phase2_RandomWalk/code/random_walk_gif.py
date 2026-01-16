import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
num_steps = 500
steps = np.random.choice([-1, 1], size=num_steps)
position = np.cumsum(steps)

fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(0, num_steps)
ax.set_ylim(min(position) - 5, max(position) + 5)
ax.set_xlabel("Step")
ax.set_ylabel("Position")
ax.set_title("1D Random Walk Evolution")

line, = ax.plot([], [], lw=2)

def update(frame):
    line.set_data(range(frame), position[:frame])
    return line,

ani = animation.FuncAnimation(
    fig, update, frames=num_steps, interval=30
)

ani.save("../graphs/random_walk.gif", writer="pillow")
plt.close()

print("Phase 2 GIF generated: random_walk.gif")

