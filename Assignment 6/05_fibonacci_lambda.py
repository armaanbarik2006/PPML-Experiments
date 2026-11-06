"""
Generate Fibonacci series using a lambda function

Python lab experiment.
Run: python 05_fibonacci_lambda.py
"""
# The lambda returns the nth Fibonacci number (0-based index).
fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)

terms = int(input("Enter number of terms: "))
if terms < 0:
    print("Number of terms cannot be negative.")
else:
    print("Fibonacci series:")
    for index in range(terms):
        print(fib(index), end=" ")
    print()
