"""
Group similar elements from a list into groups

Python lab experiment.
Run: python 01_group_similar_elements.py
"""
from collections import Counter

values = [1, 3, 5, 1, 3, 2, 5, 4, 2, 1]
counts = Counter(values)
grouped = [[value] * count for value, count in counts.items()]

print("Original list:", values)
print("Grouped elements:", grouped)
