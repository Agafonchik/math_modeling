import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

def dif_func(m, t):
    y, x = m

    dx_dt = 3*x - 2*y + np.e**(3*t) / (np.e**t + 1)

    dy_dt = x - (np.e**(3*t)) / (np.e**t + 1)

    return dy_dt, dx_dt

x0 = 5
y0 = -7
m = x0, y0

sol = odeint(dif_func, m, t)

plt.plot(t, sol[:, 1])

plt.savefig('task_2.png')