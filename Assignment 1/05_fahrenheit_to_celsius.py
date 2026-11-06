"""
Convert Fahrenheit temperature to Celsius

Python lab experiment.
Run: python 05_fahrenheit_to_celsius.py
"""
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Temperature in Celsius:", celsius)
