"""
Find roots of a quadratic equation

Python lab experiment.
Run: python 04_quadratic_equation_roots.py
"""
import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("This is not a quadratic equation because a must not be 0.")
else:
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    print("Root 1:", root1)
    print("Root 2:", root2)
