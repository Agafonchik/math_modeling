import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 100, 0.001)
g = 9.8

def radio_function(m, V):
    telo = g - k/m * V**2 
    return telo

k = 0.295
m_0 = 10
V = 15

m_t = odeint(radio_function, V, t)

plt.plot(t, m_t[:,0], label='Тело')
plt.xlabel('Время изменения скорости тела, с')
plt.ylabel('Процесс изменения положения тела, м')
plt.title('Измененения положения тела')
plt.legend()

plt.savefig('telo.png')
