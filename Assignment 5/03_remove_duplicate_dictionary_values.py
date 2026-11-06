"""
Remove duplicate values from a dictionary, keeping first occurrence

Python lab experiment.
Run: python 03_remove_duplicate_dictionary_values.py
"""
data = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}
result = {}
seen_values = set()

for key, value in data.items():
    if value not in seen_values:
        result[key] = value
        seen_values.add(value)

print("Original dictionary:", data)
print("After removing duplicate values:", result)
