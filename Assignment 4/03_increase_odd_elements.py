"""
Increase odd-valued list elements by 5

Python lab experiment.
Run: python 03_increase_odd_elements.py
"""
count = int(input("Enter number of elements: "))
numbers = []

for index in range(count):
    numbers.append(int(input(f"Enter element {index + 1}: ")))

for index in range(len(numbers)):
    if numbers[index] % 2 != 0:
        numbers[index] += 5

print("Updated list:", numbers)
