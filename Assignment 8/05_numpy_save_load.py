"""
Save and load NumPy arrays

Python lab experiment.
Run: python 05_numpy_save_load.py
"""
import numpy as np


array = np.array([1, 2, 3, 4])
np.save("my_array.npy", array)

loaded_array = np.load("my_array.npy")
print("Loaded array:", loaded_array)
