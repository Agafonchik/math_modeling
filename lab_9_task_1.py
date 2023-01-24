import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

f = np.arange(0, 100, 0.1)

def radio_function(m, f):
    bkt = k * m 
    return bkt

m_0 = 2
k = 1 / 25

m_f = odeint(radio_function, m_0, f)

plt.plot(f, m_f[:,0], label='Разделение бактерий')
plt.xlabel('Время разделения')
plt.ylabel('Количество бактерий')
plt.title('Разделение')
plt.legend()

plt.savefig('bakteriya.png')