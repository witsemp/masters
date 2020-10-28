import numpy as np
import xml.etree.cElementTree as ET
X_MIN = -0.1
X_MAX = 0.1
X_STEPS = 2
Y_MIN = -0.1
Y_MAX = 0.1
Y_STEPS = 2
Z_MIN = 0.1
Z_MAX = 0.3
Z_STEPS = 2
points = ET.Element("Points")
x_linspace = np.linspace(X_MIN, X_MAX, num=X_STEPS)
y_linspace = np.linspace(Y_MIN, Y_MAX, num=Y_STEPS)
z_linspace = np.linspace(Z_MIN, Z_MAX, num=Z_STEPS)
for x in x_linspace:
    for y in y_linspace:
        for z in z_linspace:
            point = ET.SubElement(points, "Point")
            ET.SubElement(point, "xCoord").text = str(x)
            ET.SubElement(point, "yCoord").text = str(y)
            ET.SubElement(point, "zCoord").text = str(z)
tree = ET.ElementTree(points)
tree.write("filename.xml")
