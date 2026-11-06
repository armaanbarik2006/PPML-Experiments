"""
Combine two string sets and remove duplicates

Python lab experiment.
Run: python 06_combine_sets_remove_duplicates.py
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "mango", "orange"}

combined = set1.union(set2)
print("Combined set without duplicates:", combined)
