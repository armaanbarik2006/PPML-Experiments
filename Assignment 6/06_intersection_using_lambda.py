"""
Find intersection of two lists using lambda

Python lab experiment.
Run: python 06_intersection_using_lambda.py
"""
first = [int(value) for value in input("Enter first list values: ").split()]
second = [int(value) for value in input("Enter second list values: ").split()]

intersection = list(filter(lambda value: value in first, second))
print("Intersection:", list(dict.fromkeys(intersection)))
