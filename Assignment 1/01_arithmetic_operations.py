"""
Perform arithmetic operations on two integers

Python lab experiment.
Run: python 01_arithmetic_operations.py
"""
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
if y != 0:
    print("Division:", x / y)
    print("Remainder:", x % y)
    print("Floor division:", x // y)
else:
    print("Division, remainder, and floor division are undefined when y is 0.")
