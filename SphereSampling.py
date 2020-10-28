import numpy as np
import random
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
xi, yi, zi = [], [], []
phi = np.linspace(0, np.pi, num=5)
theta = np.linspace(0, 2 * np.pi, num=10)
R = 3
for p in phi:
    for t in theta:
        x = R * np.sin(t) * np.cos(p)
        xi.append(x)
        y = R * np.sin(t) * np.sin(p)
        yi.append(y)
        z = R * np.cos(t)
        zi.append(z)

phi = np.linspace(0, np.pi, num=20)
theta = np.linspace(0, 2 * np.pi, num=40)
x = R*np.outer(np.sin(theta), np.cos(phi))
y = R*np.outer(np.sin(theta), np.sin(phi))
z = R*np.outer(np.cos(theta), np.ones_like(phi))
fig, ax = plt.subplots(1, 1, subplot_kw={'projection':'3d', 'aspect':'auto'})
ax.plot_wireframe(x, y, z, color='k', rstride=1, cstride=1)
ax.scatter(xi, yi, zi, s=100, c='r', zorder=10)
plt.show()
