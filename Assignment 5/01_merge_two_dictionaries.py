"""
Merge two dictionaries

Python lab experiment.
Run: python 01_merge_two_dictionaries.py
"""
first = {"a": 10, "b": 20}
second = {"c": 30, "d": 40}

merged = first.copy()
merged.update(second)

print("First dictionary:", first)
print("Second dictionary:", second)
print("Merged dictionary:", merged)
