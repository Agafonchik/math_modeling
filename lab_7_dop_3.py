import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

star, = plt.plot([], [], '-', color='r', label='Star')

alpha = np.arange(0, 4*np.pi, 0.1)
x = 12 * np.cos(alpha) + 8 * np.cos(1.5 * alpha)
y = 12 * np.sin(alpha) - 8 * np.sin(1.5 * alpha)

def rotate(t):
    t = t * np.pi / 180
    X = x * np.cos(t) - y * np.sin(t)
    Y = y * np.cos(t) + x * np.sin(t)
    return X, Y

def animate(i):
    star.set_data(rotate(t=i))
    return x, y

edge = 25
plt.axis('equal')
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)
 
ani = FuncAnimation(fig, animate, frames=200, interval=30)
ani.save('lab_7_dop_3.gif')