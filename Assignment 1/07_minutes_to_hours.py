"""
Convert minutes into hours and minutes

Python lab experiment.
Run: python 07_minutes_to_hours.py
"""
minutes = int(input("Enter time in minutes: "))
if minutes < 0:
    print("Time cannot be negative.")
else:
    hours = minutes // 60
    remaining_minutes = minutes % 60
    print(hours, "hour(s) and", remaining_minutes, "minute(s)")
