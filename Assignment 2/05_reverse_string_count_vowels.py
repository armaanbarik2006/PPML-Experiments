"""
Reverse a string and count vowels and consonants

Python lab experiment.
Run: python 05_reverse_string_count_vowels.py
"""
text = input("Enter a string: ")
print("Reversed string:", text[::-1])

vowels = sum(1 for char in text if char.isalpha() and char.lower() in "aeiou")
consonants = sum(1 for char in text if char.isalpha() and char.lower() not in "aeiou")

print("Vowels:", vowels)
print("Consonants:", consonants)
