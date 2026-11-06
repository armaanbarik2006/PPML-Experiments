"""
Display grade based on percentage

Python lab experiment.
Run: python 01_percentage_to_grade.py
"""
percentage = float(input("Enter percentage (0-100): "))

if not 0 <= percentage <= 100:
    print("Please enter a percentage between 0 and 100.")
elif percentage >= 90:
    print("Grade: O")
elif percentage >= 80:
    print("Grade: E")
elif percentage >= 70:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F")
