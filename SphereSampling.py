import numpy as np
from matplotlib import pyplot as plt
import xml.etree.cElementTree as ET


def generate_from_sphere(phi_steps: int, theta_steps: int, r: float, visualize=True):
    xi, yi, zi = [], [], []
    points = ET.Element("Points")
    # horizontal linspace
    phi = np.linspace(0, 2 * np.pi, num=2*phi_steps)
    # vertical linspace
    theta = np.linspace(0, np.pi, num=theta_steps)
    for t in theta:
        for p in phi:
            z = r * np.cos(t)
            if 0 < z < r:
                zi.append(z)
                x = r * np.sin(t) * np.cos(p)
                xi.append(x)
                y = r * np.sin(t) * np.sin(p)
                yi.append(y)
                point = ET.SubElement(points, "Point")
                ET.SubElement(point, "xCoord").text = str(x)
                ET.SubElement(point, "yCoord").text = str(y)
                ET.SubElement(point, "zCoord").text = str(z)
            else:
                continue
    tree = ET.ElementTree(points)
    tree.write("filename.xml")
    print("Number of points in upper part of sphere: ", len(zi))

    if visualize:
        phi = np.linspace(0, np.pi, num=20)
        theta = np.linspace(0, 2 * np.pi, num=40)
        x = r * np.outer(np.sin(theta), np.cos(phi))
        y = r * np.outer(np.sin(theta), np.sin(phi))
        z = r * np.outer(np.cos(theta), np.ones_like(phi))
        fig, ax = plt.subplots(1, 1, subplot_kw={'projection': '3d', 'aspect': 'auto'})
        ax.plot_wireframe(x, y, z, color='k', rstride=1, cstride=1)
        ax.scatter(xi, yi, zi, s=100, c='r', zorder=10)
        plt.show()


if __name__ == '__main__':
    generate_from_sphere(phi_steps=30, theta_steps=40, r=1.35, visualize=True)
