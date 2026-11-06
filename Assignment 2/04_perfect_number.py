"""
Check whether a number is perfect

Python lab experiment.
Run: python 04_perfect_number.py
"""
number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    divisor_sum = sum(i for i in range(1, number) if number % i == 0)
    if divisor_sum == number:
        print("It is a perfect number.")
    else:
        print("It is not a perfect number.")
