import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)

def dif_func(m, x):
    y, z = m

    dy_dx = y**2 * z

    dz_dx = z / x - y * z**2

    return dy_dx, dz_dx

y0 = 1
z0 = -3
m = y0, z0

sol = odeint(dif_func, m, x)

plt.plot(x, sol[:, 1])

plt.savefig('task_1.png')
