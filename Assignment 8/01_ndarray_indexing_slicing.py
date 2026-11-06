"""
NumPy ndarray object, indexing, and slicing

Python lab experiment.
Run: python 01_ndarray_indexing_slicing.py
"""
import numpy as np


array = np.array([[10, 20, 30], [40, 50, 60]])

print("Array:\n", array)
print("Element at row 0, column 1:", array[0, 1])
print("Second row:", array[1, :])
print("Third column:", array[:, 2])
