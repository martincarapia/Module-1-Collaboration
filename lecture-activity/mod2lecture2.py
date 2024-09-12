"""
Write a program that takes a student’s score as input and prints their grade based on the following criteria:

90 and above A
80 to 89: B
70 to 79: C
60 to 69: D
Below 60: F
"""

score = int(input("Please enter a score to get your grade: "))

if score >= 90:
    print("You got an A")
elif score >= 80:
    print("You got a B")
elif score >= 70:
    print("You got a C")
elif score >= 60:
    print("You got a D")
else:
    print("You got an F")