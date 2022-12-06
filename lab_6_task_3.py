# Создать функцию, строящую график эллипса.
# На вход, функции подаются пределы изменения переменной x и количество точек N, на которое разбиваются соответствующие пределы.

import matplotlib.pyplot as plt
import numpy as np

def ellips(b=1, c=1, title='Ellips'):
    x = np.arange()