"""
Check whether a string is a palindrome

Python lab experiment.
Run: python 04_string_palindrome.py
"""
text = input("Enter a string: ")
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
