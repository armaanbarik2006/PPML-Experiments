"""
Return even values from a list using a function

Python lab experiment.
Run: python 05_function_return_even_values.py
"""
def even_values(values):
    return [value for value in values if value % 2 == 0]

numbers = [int(value) for value in input("Enter integers separated by spaces: ").split()]
print("Even values:", even_values(numbers))
