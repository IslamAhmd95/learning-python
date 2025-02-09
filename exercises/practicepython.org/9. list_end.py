"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
"""

import random

def list_first_last(numbers: list) -> list:
    """Returns a list containing the first and last elements of the given list."""
    return [numbers[0], numbers[-1]]

# Generate a list of 10 random numbers between 0 and 100
numbers = random.sample(range(0, 100), 10)  # No duplicates
# numbers = random.choices(range(0, 100), k=10)  # Allows duplicates

print("Original list:", numbers)
print("First and last elements:", list_first_last(numbers))
