import matplotlib.pyplot as plt 

def square(title='square'):
    plt.plot([1, 1, 5, 5, 1], [5, 1, 1, 5, 5])
    plt.axis('equal')
    plt.title(title)
    plt.savefig('pu.png')
square()

plt.plot([1, 1, 5, 5, 1], [5, 1, 1, 5, 5])
plt.savefig('pu3.png')
