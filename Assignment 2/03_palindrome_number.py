"""
Check whether an integer is a palindrome

Python lab experiment.
Run: python 03_palindrome_number.py
"""
number = input("Enter an integer: ")
if number.startswith("-"):
    print("Negative numbers are not treated as palindromes in this program.")
elif number == number[::-1]:
    print("It is a palindrome number.")
else:
    print("It is not a palindrome number.")
