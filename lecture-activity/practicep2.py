"""
Write a program that checks if a given year is a leap year. A year is a leap year if:

It is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
"""

year = int(input("Enter a year:"))

if (year % 400) == 0 or (year % 4) == 0 and (year % 100) != 0:
    print("Leap year")
else:
    print("Not a leap year")