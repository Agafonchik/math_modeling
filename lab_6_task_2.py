# Создать функцию, строящую график гиперболы, заданной явно.
# На вход, функции подаются пределы изменения переменной x и количество точек N, на которое разбиваются соответствующие пределы.

import matplotlib.pyplot as plt
import numpy as np

def giperbola_plotter(k=1, title='Giperbola'):
    x = np.arange(0.1, 5, 0.1)
    y = k / x
    plt.plot(x, y, label='my giperbola')
    plt.xlabel('Coord - x')
    plt.ylabel('Coord - y')
    plt.title(title)
    plt.grid()
    plt.axis('equal')
    plt.legend()
    plt.savefig('frik.png') 
giperbola_plotter()