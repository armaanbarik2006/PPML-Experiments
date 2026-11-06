"""
Draw histograms and box plots

Python lab experiment.
Run: python 03_histogram_and_box_plot.py
"""
import matplotlib.pyplot as plt


# Histogram
histogram_data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5]
plt.hist(histogram_data, bins=5, label="Histogram data")
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Box plot
box_data = [7, 8, 5, 6, 9, 10, 15, 20, 21]
plt.boxplot(box_data)
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()
