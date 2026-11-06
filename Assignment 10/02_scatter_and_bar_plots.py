"""
Draw scatter and bar plots

Python lab experiment.
Run: python 02_scatter_and_bar_plots.py
"""
import matplotlib.pyplot as plt


# Scatter plot
x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 7]

plt.scatter(x, y, label="Scatter points")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# Bar plot
categories = ["A", "B", "C", "D"]
values = [3, 7, 8, 5]

plt.bar(categories, values, label="Bar data")
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()
plt.show()
