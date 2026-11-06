"""
Print twin prime pairs between 1 and N

Python lab experiment.
Run: python 01_twin_primes.py
"""
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True

limit = int(input("Enter N: "))
print("Twin prime pairs:")
for number in range(2, limit - 1):
    if is_prime(number) and is_prime(number + 2):
        print(f"({number}, {number + 2})")
