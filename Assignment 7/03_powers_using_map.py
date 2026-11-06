"""
Calculate corresponding powers using map()

Python lab experiment.
Run: python 03_powers_using_map.py
"""
bases = [int(value) for value in input("Enter bases: ").split()]
exponents = [int(value) for value in input("Enter corresponding exponents: ").split()]

if len(bases) != len(exponents):
    print("The lists must have the same length.")
else:
    result = list(map(pow, bases, exponents))
    print("Powers:", result)
