import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
t = np.arange(0, 10, 0.01)

# Определяем функцию для системы диф. уравнений
def diff_func(z, t): # z - изменяемая величина для системы
    theta, omega = z

    dtheta_dt = omega

    domega_d = - b * np.sin(theta)

    return dtheta_dt, domega_d

# Определяем начальные значения и параметры,
# входящие в систему диф. уравнений
theta0 = np.pi - 0.1
omega0 = 0

# Начальное значение изменяемой величины системы
z0 = theta0, omega0

b = 0.25
c = 5.0

# Решаем систему диф. уравнений
sol = odeint(diff_func, z0, t)

# Строим решение в виде графика
plt.plot(t, sol[:, 1], 'b', label='theta(t)')

plt.legend()
plt.savefig('func(t).png')


plt.plot(sol[:, 1], sol[:, 0], 'g', label='theta(omega)')

plt.legend()
plt.savefig('по другому.png')