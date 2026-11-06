"""
Search for an element in a list using a lambda function

Python lab experiment.
Run: python 04_search_list_using_lambda.py
"""
values = [int(value) for value in input("Enter list values separated by spaces: ").split()]
target = int(input("Enter the value to search for: "))

is_target = lambda value: value == target
found = any(map(is_target, values))

if found:
    print(target, "is present in the list.")
else:
    print(target, "is not present in the list.")
