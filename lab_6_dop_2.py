import matplotlib.pyplot as plt
import numpy as np

def ellips(b, a):
    f = np.arange(0, 25, 0.1)
    p = b**2 / a
    r = p / (1 + np.e * np.cos(f))
    x = r * np.cos(f)
    y = r * np.sin(f)
    
    plt.contour(x, y, r, levels=[0])
    plt.legend()
    plt.savefig('pic_8.png')
ellips(2, 3)