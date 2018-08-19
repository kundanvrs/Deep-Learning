from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.axes3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()


def f1(x):
    return 1/(1+np.exp(-(400*x+24)))
def f2(x):
    return 1/(1+np.exp(-(400*x-24)))
def f(x):
    return f1(x)-f2(x)
x = np.linspace(-1, 1, 50)


X,Y = np.meshgrid(x, y)
z = f(x)
print(max(z))
ax = plt.axes()
ax.plot(x, z )
plt.show()
