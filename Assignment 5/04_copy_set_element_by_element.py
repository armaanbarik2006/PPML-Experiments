"""
Copy set elements into a new set one at a time

Python lab experiment.
Run: python 04_copy_set_element_by_element.py
"""
original = {10, 20, 30, 40}
copied = set()

for element in original:
    copied.add(element)

print("Original set:", original)
print("Copied set:", copied)
