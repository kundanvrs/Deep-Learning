from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.axes3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
#finding the value of h11

def h11(x, y):
    return 1/(1+np.exp(-(x+100*y+200)))
def h12(x, y):
    return 1/(1+np.exp(-(x+100*y-200)))
def h13(x, y):
    return 1/(1+np.exp(-(100*x+y+200)))
def h14(x, y):
    return 1/(1+np.exp(-(x+100*y-200)))
def h21(x , y):
	return h11(x , y) - h12(x , y)
def h22(x , y):
	return h13(x , y) - h14(x , y)
def h31(x , y):
	return h21(x , y) + h22(x , y)

def f(x, y):
    return 1/(1+np.exp(-(50*h31(x, y)- 100)))

#all points
x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)

X, Y = np.meshgrid(x, y) #all the grids
Z = f(X, Y)

z1 = h31(X, Y)
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z )
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('f(X1 , X2)')
plt.show()
