"""
Print Fibonacci series using a function without recursion

Python lab experiment.
Run: python 04_fibonacci_function_iterative.py
"""
def fibonacci(count):
    a, b = 0, 1
    for _ in range(count):
        print(a, end=" ")
        a, b = b, a + b
    print()

terms = int(input("Enter number of terms: "))
if terms < 0:
    print("Number of terms cannot be negative.")
else:
    fibonacci(terms)
