import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
cyc, = plt.plot([], [], 'o', color='b', label='Ball')
traj, = plt.plot([], [], 'o', color='b', label='Ball')

def cycloida(R, time):
    x = R * (time - np.sin(time))
    y = R * (1 - np.cos(time))
    return x, y

def tz_move(R, vx0, vy0, time):
    x0 = vx0 * time + R
    y0 = vy0 * time + R
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha) - R
    y = y0 + R*np.sin(alpha)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

x, y = [], []

def animate(i):
    ball.set_data(tz_move(R=0.5, vx0=0.01, vy0=0, time=i))
    coords = cycloida(R=0.5, time=i/30)
    x.append(coords[0])
    y.append(coords[1])
    cyc.set_data(x[i], y[i])
    traj.set_data(x, y)

ani = FuncAnimation(fig, animate, frames=200, interval=100)

ani.save('lab_7_dop_1.gif')

fig, ax = plt.subplots()

aster, = plt.plot([], [], 'o', color='b', label='Ball')
trajictor, = plt.plot([], [], 'o', color='b', label='Ball')

def asteroida(R, time):
    x = R * np.cos(time)**3
    y = R * np.sin(time)**3
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

x, y = [], []

def animate(i):
    coords = asteroida(R=0.5, time=i/10)
    x.append(coords[0])
    y.append(coords[1])
    aster.set_data(x[i], y[i])
    trajictor.set_data(x, y)

ani = FuncAnimation(fig, animate, frames=100, interval=100)

ani.save('lab_7_dop_1_2.gif')
