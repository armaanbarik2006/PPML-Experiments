"""
Print digits at odd positions in a five-digit number (left to right)

Python lab experiment.
Run: python 02_odd_position_digits.py
"""
number = input("Enter a 5-digit number: ")

if not number.isdigit() or len(number) != 5:
    print("Please enter exactly five digits.")
else:
    print("Digits at odd positions (1, 3, 5):")
    for index in range(0, 5, 2):
        print(number[index])
