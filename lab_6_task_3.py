import matplotlib.pyplot as plt
import numpy as np

def ellips_plotter(b, a):
    x = np.arange(-2*a, a, 0.1)
    y = np.arange(-a, a, 0.1)
    X, Y = np.meshgrid(x, y)

    fxy = X**2 / a**2 + Y**2 / b**2 - 1
    plt.contour(X, Y, fxy, levels=[0])
    plt.savefig('fignya.png')
ellips_plotter(2, 3)