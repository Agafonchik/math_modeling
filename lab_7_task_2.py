import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

mus, = plt.plot([], [], 'o', color='r', label='Mus')

def update(R):
    al = np.arange(0, 2*np.pi, 0.1)
    x = R*np.cos(al)
    y = R*np.sin(al)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    mus.set_data(circle_move(R=i))

ani = FuncAnimation(fig, update, frames=np.arange(0, 3, 0.1), interval=100)

ani.save('mus.gif')