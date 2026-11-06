"""
Calculate the area of a triangle using Heron's formula

Python lab experiment.
Run: python 02_triangle_area_heron.py
"""
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of triangle:", area)
else:
    print("The given sides do not form a triangle.")
