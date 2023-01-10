import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() #создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw=2) # объект анимации

xdata, ydata = [], [] # координаты объекта анимации

ax.set_xlim(0, 2*np.pi) # Пределы изменения переменной Х
ax.set_ylim(-1, 1) # Пределы изменения переменной У
 
def update(frame): # Функция подстановки координат в объект анимации
    xdata.append(frame) # Расчет координаты Х
    ydata.append(np.sin(frame)) # Расчет координаты У
    anim_object.set_data(xdata, ydata) # Передача координат
    return anim_object,

ani = FuncAnimation(fig, update, frames=np.arange(0,12*np.pi, 0.1), interval=100)

ani.save('поперечная волна.gif')