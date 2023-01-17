import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots()

but, = plt.plot([], [], '-', color='r', label='Butr')

def but_move(t):
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + np.sin(t / 12)**5)
    y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + np.sin(t / 12)**5)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

x = []
y = []

def animate(i):
    x.append(but_move(t=i)[0])
    y.append(but_move(t=i)[1])
    but.set_data(x, y)

ani = FuncAnimation(fig, animate, frames=np.arange(0.1, 2*np.pi, 0.1), interval=30)
ani.save('but.gif')


re, = plt.plot([], [], '-', color='r', label='Re')

def re_move(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def animate(i):
    x.append(re_move(t=1)[0])
    y.append(re_move(t=1)[1])
    re.set_data(re_move(x, y))

ani = FuncAnimation(fig, animate, frames=100, interval=30)

plt.savefig('re.gif')