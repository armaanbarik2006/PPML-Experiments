"""
NumPy array properties and functions

Python lab experiment.
Run: python 03_numpy_array_properties_functions.py
"""
import numpy as np


ones_array = np.ones((2, 3))
zeros_array = np.zeros((2, 3))
empty_array = np.empty((2, 3))

print("Ones:\n", ones_array)
print("Zeros:\n", zeros_array)
print("Empty (values are uninitialized):\n", empty_array)

array = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape:", array.shape)
print("Reshaped array:\n", array.reshape(3, 2))

original = np.array([1, 2, 3])
copy_array = original.copy()
view_array = original.view()
print("Original:", original)
print("Copy:", copy_array)
print("View:", view_array)

combined = np.concatenate((np.array([1, 2]), np.array([3, 4])))
print("Concatenated array:", combined)
print("Sorted array:", np.sort(np.array([5, 2, 9, 1])))
