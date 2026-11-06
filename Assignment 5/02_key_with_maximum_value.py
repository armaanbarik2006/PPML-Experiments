"""
Find the key having the maximum value in a dictionary

Python lab experiment.
Run: python 02_key_with_maximum_value.py
"""
data = {"A": 45, "B": 72, "C": 61, "D": 90}

if data:
    maximum_key = max(data, key=data.get)
    print("Key with maximum value:", maximum_key)
    print("Maximum value:", data[maximum_key])
else:
    print("Dictionary is empty.")
