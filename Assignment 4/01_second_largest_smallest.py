"""
Find second-largest and second-smallest distinct values without sort()

Python lab experiment.
Run: python 01_second_largest_smallest.py
"""
numbers = []
count = int(input("How many integers? "))

for index in range(count):
    numbers.append(int(input(f"Enter element {index + 1}: ")))

unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

if len(unique_numbers) < 2:
    print("At least two distinct values are required.")
else:
    largest = second_largest = float("-inf")
    smallest = second_smallest = float("inf")

    for number in unique_numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest:
            second_largest = number

        if number < smallest:
            second_smallest = smallest
            smallest = number
        elif number < second_smallest:
            second_smallest = number

    print("Second largest:", second_largest)
    print("Second smallest:", second_smallest)
