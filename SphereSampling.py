import numpy as np
from matplotlib import pyplot as plt
import xml.etree.cElementTree as ET
xi, yi, zi = [], [], []
points = ET.Element("Points")
phi = np.linspace(0, 2* np.pi, num=60)
theta = np.linspace(0, 2 * np.pi, num=60)
R = 1.35
for t in theta:
    for p in phi:
        z = R * np.cos(t)
        if 0 < z < R:
            zi.append(z)
            x = R * np.sin(t) * np.cos(p)
            xi.append(x)
            y = R * np.sin(t) * np.sin(p)
            yi.append(y)
            point = ET.SubElement(points, "Point")
            ET.SubElement(point, "xCoord").text = str(x)
            ET.SubElement(point, "yCoord").text = str(y)
            ET.SubElement(point, "zCoord").text = str(z)
        else:
            continue
tree = ET.ElementTree(points)
tree.write("filename.xml")


phi = np.linspace(0, np.pi, num=20)
theta = np.linspace(0, 2 * np.pi, num=40)
x = R*np.outer(np.sin(theta), np.cos(phi))
y = R*np.outer(np.sin(theta), np.sin(phi))
z = R*np.outer(np.cos(theta), np.ones_like(phi))
fig, ax = plt.subplots(1, 1, subplot_kw={'projection':'3d', 'aspect':'auto'})
ax.plot_wireframe(x, y, z, color='k', rstride=1, cstride=1)
ax.scatter(xi, yi, zi, s=100, c='r', zorder=10)
plt.show()
