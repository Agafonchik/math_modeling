import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

xdata, ydata = [], []

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)
 
def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    anim_object.set_data(xdata, ydata)
    return anim_object,

ani = FuncAnimation(fig, update, frames=np.arange(0,12*np.pi, 0.1), interval=100)

ani.save('поперечная волна.gif')

import matplotlib.pyplot as plt
import numpy as np

x = [0, 4, 10]
y = [0, 0, 0]

plt.plot(x, y, color='red', label='luchte', marker='>', ms=5)
plt.xlabel('Coord: x')
plt.ylabel('Coord: y')
plt.legend()
plt.title('Продольная и поперечная волны')
plt.grid()
plt.savefig('две волны.png')