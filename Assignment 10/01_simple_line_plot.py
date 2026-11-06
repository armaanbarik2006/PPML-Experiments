"""
Draw a simple line graph using plot()

Python lab experiment.
Run: python 01_simple_line_plot.py
"""
import matplotlib.pyplot as plt


x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, linestyle="--", marker="o", label="Data line")
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
