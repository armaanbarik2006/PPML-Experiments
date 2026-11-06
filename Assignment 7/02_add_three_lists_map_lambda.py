"""
Add corresponding elements of three lists using map() and lambda

Python lab experiment.
Run: python 02_add_three_lists_map_lambda.py
"""
first = [int(value) for value in input("Enter first list: ").split()]
second = [int(value) for value in input("Enter second list: ").split()]
third = [int(value) for value in input("Enter third list: ").split()]

if not (len(first) == len(second) == len(third)):
    print("All three lists must have the same length.")
else:
    result = list(map(lambda a, b, c: a + b + c, first, second, third))
    print("Resultant list:", result)
