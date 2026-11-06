"""
Find factorial of a number using a loop

Python lab experiment.
Run: python 02_factorial.py
"""
number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for value in range(1, number + 1):
        factorial *= value
    print(f"Factorial of {number} is {factorial}")
