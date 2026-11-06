"""
Triple all numbers in a list using map()

Python lab experiment.
Run: python 01_triple_numbers_using_map.py
"""
numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
tripled = list(map(lambda number: number * 3, numbers))
print("Tripled list:", tripled)
