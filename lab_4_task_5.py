#Создать функцию, определяющую площади круга, прямоугольника и треугольника по соответствующим параметрам,
#  в зависимости от того, какую фигуру выберет пользователь.

import numpy as np

def ty(a, b, h, R):
    P = a * b
    T = 0.5 * a * h
    K = np.pi * R ** 2
    print(P, T, K)
    return a * b, 0.5 * a * h, np.pi * R ** 2
ty(2, 3, 5, 6)

# Правильный пример работы
def area(*arg, **kw):
    if kw['figure'] == 'square':
        s = arg[0] ** 2
    elif kw['figure'] == 'rectangle':
        s = arg[0] * arg[1]
    else:
        s = 1 / 2 * arg[0] * arg[1]
        print(s)
area(2, 3, 5, 8, figure='square')