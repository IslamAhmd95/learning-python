"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

import datetime

name = input("Enter your name: ").strip().title()  # .title() makes it "John Doe" instead of "JOHN DOE"

try:
    age = int(input("Enter your age : ").strip())
    if age <= 0:
        print("Invalid age. Please enter a realistic number.")
        exit()
except ValueError:
    print("Invalid input. Age should be a number.")
    exit()

try:
    repeat_count = int(input("Enter a number (how many times to print the message): ").strip())
    if repeat_count <= 0:
        print("Invalid repeat count. Please enter a positive number.")
        exit()
except ValueError:
    print("Invalid input. Repeat count should be a number.")
    exit()

current_year = datetime.datetime.now().year
target_year = current_year + (100 - age)
message = f"Hello {name}, you will turn 100 years old in the year {target_year}.\n"

print(repeat_count * message)
