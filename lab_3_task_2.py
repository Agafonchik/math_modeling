import lab_3_task_1.py
import numpy as np 

h = 100
a = np.pi / 3
b = 30
V = np.sqrt((g*t*np.tan(b)**2) / 2*np.cos(a)**2 * (1 - np.tan(b)*np.tan(a)))
print(V)

from lab_3_task_1.py import h, k, T, e, E
N = 2 / np.sqrt(np.pi) * (h / (k*T)**1.5) * e**(E/(k*T)) * e**(T/2)
print(N)