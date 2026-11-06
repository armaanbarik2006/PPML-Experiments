"""
Draw pie charts and contour plots

Python lab experiment.
Run: python 04_pie_and_contour_plots.py
"""
import matplotlib.pyplot as plt


import numpy as np

# Pie chart
sizes = [15, 30, 45, 10]
labels = ["A", "B", "C", "D"]
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%",
        shadow=True, startangle=140)
plt.title("Pie Chart")
plt.axis("equal")
plt.show()

# Contour plot
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

contour = plt.contour(X, Y, Z, levels=10)
plt.title("Contour Plot")
plt.colorbar(contour)
plt.show()
