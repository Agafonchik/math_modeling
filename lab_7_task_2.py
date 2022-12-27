import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

mus, = plt.plot([], [], '-', color='r', label='Mus')

def circle_move(R):
    al = np.arange(0, 2*np.pi, 0.1)
    x = R*np.cos(al)
    y = R*np.sin(al)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    mus.set_data(circle_move(R=0.025 * i))

ani = FuncAnimation(fig, animate, frames=100, interval=30)

ani.save('mus.gif')