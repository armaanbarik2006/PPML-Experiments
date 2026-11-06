"""
Change character case using map() and remove duplicates

Python lab experiment.
Run: python 04_swap_case_remove_duplicates_map.py
"""
characters = input("Enter characters without separators: ")
converted = list(map(lambda char: char.lower() if char.isupper() else char.upper(), characters))
unique_characters = list(dict.fromkeys(converted))

print("Case-converted characters:", converted)
print("After removing duplicates:", unique_characters)
