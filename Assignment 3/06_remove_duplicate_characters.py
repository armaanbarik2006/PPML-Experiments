"""
Remove duplicate characters from a string, preserving order

Python lab experiment.
Run: python 06_remove_duplicate_characters.py
"""
text = input("Enter a string: ")
result = ""

for character in text:
    if character not in result:
        result += character

print("String after removing duplicates:", result)
