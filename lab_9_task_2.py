import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 15, 0.01)

def radio_function(I, t):
    inv = - k * I * t
    return inv

k = 0.08
I_0 = 1000

I_t = odeint(radio_function, I_0, t)

plt.plot(t, I_t[:,0], label='Инвестиции')
plt.xlabel('Время изменения инвестиций')
plt.ylabel('Процесс изменения инвестиций')
plt.title('Измененения инвестиций')
plt.legend()

plt.savefig('investiciya.png')