import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.01)

def dif_func(m, t):
    y, x = m
    dydt = x
    dxdt = np.sin(x) + np.cos(x)

    return dydt, dxdt

x0 = 0
y0 = 3
m0 = y0, x0

sol = odeint(dif_func, m0, t)

plt.plot(t, sol[:, 1])

plt.savefig('task_3.png')