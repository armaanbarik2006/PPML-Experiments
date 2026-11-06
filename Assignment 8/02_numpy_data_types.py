"""
NumPy data types and structures

Python lab experiment.
Run: python 02_numpy_data_types.py
"""
import numpy as np


array = np.array([1, 2, 3], dtype="int32")
print("Original array:", array)
print("Original data type:", array.dtype)

float_array = array.astype("float64")
print("Converted array:", float_array)
print("Updated data type:", float_array.dtype)
