"""
Statistical operations and broadcasting on NumPy arrays

Python lab experiment.
Run: python 04_numpy_statistics_broadcasting.py
"""
import numpy as np


array = np.array([1, 2, 3, 4])

print("Maximum:", array.max())
print("Minimum:", array.min())
print("Sum:", array.sum())
print("Product:", array.prod())
print("Broadcasted result (array + 5):", array + 5)
