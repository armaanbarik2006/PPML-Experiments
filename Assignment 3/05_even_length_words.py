"""
Print words having even length

Python lab experiment.
Run: python 05_even_length_words.py
"""
sentence = input("Enter a sentence: ")
words = sentence.split()

print("Even-length words:")
for word in words:
    if len(word) % 2 == 0:
        print(word)
