from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.axes3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')

def f(x, y):
    return 1/(1+np.exp(-(x+100*y+200)))
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z )
plt.show()
