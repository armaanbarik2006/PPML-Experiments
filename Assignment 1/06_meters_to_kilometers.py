"""
Convert meters into kilometers and remaining meters

Python lab experiment.
Run: python 06_meters_to_kilometers.py
"""
meters = int(input("Enter distance in meters: "))
if meters < 0:
    print("Distance cannot be negative.")
else:
    kilometers = meters // 1000
    remaining_meters = meters % 1000
    print(kilometers, "kilometer(s) and", remaining_meters, "meter(s)")
