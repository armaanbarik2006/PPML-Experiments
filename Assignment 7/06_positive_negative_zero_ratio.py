"""
Find ratios of positive, negative, and zero values using filter() and map()

Python lab experiment.
Run: python 06_positive_negative_zero_ratio.py
"""
numbers = [int(value) for value in input("Enter integers: ").split()]

if not numbers:
    print("Please enter at least one integer.")
else:
    total = len(numbers)
    positive = len(list(filter(lambda value: value > 0, numbers)))
    negative = len(list(filter(lambda value: value < 0, numbers)))
    zeros = len(list(filter(lambda value: value == 0, numbers)))

    ratios = list(map(lambda count: round(count / total, 2), [positive, negative, zeros]))
    print("Ratios [positive, negative, zero]:", ratios)
