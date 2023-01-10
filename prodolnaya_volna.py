import matplotlib.pyplot as plt
import numpy as np

x = [0, 4, 10]
y = [0, 0, 0]

plt.plot(x, y, color='red', label='luchte', marker='>', ms=5)
plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.legend()
plt.title('Продольна волна')
plt.grid()
plt.savefig('продольная волна.png')