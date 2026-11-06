"""
Combine elements from two lists alternately

Python lab experiment.
Run: python 02_combine_two_lists_alternately.py
"""
numbers = [1, 2, 3, 4, 5]
letters = ["A", "B", "C", "D", "E"]

combined = []
for number, letter in zip(numbers, letters):
    combined.extend([number, letter])

print("Combined list:", combined)
