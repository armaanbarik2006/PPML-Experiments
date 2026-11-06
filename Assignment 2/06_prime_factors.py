"""
Print the prime factors of a three-digit number

Python lab experiment.
Run: python 06_prime_factors.py
"""
number = int(input("Enter a three-digit positive integer: "))

if not 100 <= number <= 999:
    print("Please enter a positive three-digit integer.")
else:
    n = number
    factor = 2
    print("Prime factors:", end=" ")
    while factor * factor <= n:
        while n % factor == 0:
            print(factor, end=" ")
            n //= factor
        factor += 1
    if n > 1:
        print(n, end="")
    print()
