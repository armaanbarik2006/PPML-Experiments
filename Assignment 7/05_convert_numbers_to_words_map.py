"""
Convert integers from 0 to 9 into words using map()

Python lab experiment.
Run: python 05_convert_numbers_to_words_map.py
"""
number_words = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
}

def convert(number):
    return number_words.get(number, "out of range")

numbers = [int(value) for value in input("Enter integers from 0 to 9: ").split()]
print("Words:", list(map(convert, numbers)))

number_tuple = tuple(numbers)
print("Tuple converted to words:", list(map(convert, number_tuple)))
