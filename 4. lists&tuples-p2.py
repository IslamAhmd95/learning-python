# List comprehension not compression

"""
List comprehension in Python is a concise way to create lists. It uses a single line of code to define and manipulate the elements of the list based on a given expression.

Here’s the syntax:

new_list = [expression for item in iterable if condition]
expression: The operation or value to include in the new list.
for item in iterable: Iterates through the given sequence (e.g., a list, range, string, etc.).
if condition (optional): Filters elements based on a condition.

"""

# example
fruits = ["banana", "orange", "strawberry", "apple", "Boysenberry", "Lemon"]
fruitsHasA = [x if "a" in x else "no a" for x in fruits]
print(fruitsHasA)  # ['banana', 'orange', 'strawberry', 'apple', 'no a', 'no a']


# example
word = "RED"
listOfChars = [x*3 for x in word]
print(listOfChars)  # ['RRR', 'EEE', 'DDD']


# example
words = [" RED", "Yellow ", "  Green   "]
strippedWords = [x.strip() for x in words]
print(strippedWords)  # ['RED', 'Yellow', 'Green']


# example: Create a list of squares of numbers from 0 to 9:
squares = [x**2 for x in range(10)]
print(squares)


# example: even numbers between 0 and 20
evenNumbers = [x for x in range(21) if x % 2 == 0]
print(evenNumbers)


# example: Convert a list of strings to uppercase:
strings = ["python", "is", "beautiful"]
upperStrings = [word.upper() for word in strings]
print(upperStrings)


# example: Remove duplicates from a list:
original_list = [1, 2, 3, 4, 1, 3, 5]
# unique_list = [x for i, x in enumerate(original_list) if x not in original_list[:i]]
# Performance:
# This approach is straightforward but inefficient for large lists. For every element, it checks membership in a slice of increasing size (O(n^2) in the worst case).
seen = set()
unique_list = [x for x in original_list if x not in seen and not seen.add(x)]
# If x is not in seen, the second part of the condition (not seen.add(x)) adds x to seen.
# seen.add(x) returns None, I have to use not so the condition remains True.
# Performance:
# This approach is more efficient because set lookups and additions are O(1) on average. The overall complexity is O(n).
print(unique_list)


# example: Generate all combinations of two lists:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combinedList = [x for x in list1 + list2]
print(combinedList)
listsPairs = [(x, y) for x in list1 for y in list2]
# x corresponds to the first for loop: for x in list1.
# y corresponds to the second for loop: for y in list2.
print(listsPairs) # [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]


# example: Get numbers between 1 and 50 divisible by both 3 and 5:
filteredNumbers = [x for x in range (1, 51) if (x % 3 == 0 and x % 5 == 0)]
print(filteredNumbers)  # [15, 30, 45]


# example: Find the sum of squares of numbers in a list:
# sum = sum([x**2 for x in range(1, 4)])
import functools
sum = functools.reduce(lambda acc, x: acc + x, [x**2 for x in range(1, 4)])
print(sum)  # 14


# example: Flatten a 2D, 3D list (a list of lists):
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
flattened = [item for sublist in matrix for item in sublist]
#  is the same as the below code
# flattened = []
# for sublist in matrix:  # first loop from the list comprehension
#     for item in sublist: # second loop from the list comprehension
#         flattened.append(item)  # item to be returned
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8]


ThreeDList = [[[0, 1], [2, 3], [4, 5, 6], [7, 8], [9, 10]], [[11, 12]]]
flattened3D = [item for sublist in ThreeDList for subsublist in sublist for item in subsublist]
print(flattened3D)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


# example: apply function to list comprehension iterms:
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4]
squared_numbers = [square(x) for x in numbers]
print(squared_numbers)  # [1, 4, 9, 16]


# example
keys = 'abc'
values = [1, 2, 3, 4]
pairs = [(x, y) for x, y in zip(keys, values)]
print(pairs)  # [('a', 1), ('b', 2), ('c', 3)]


# example: prime numbers beteen 2 and 50:
primes = [x for x in range(2, 51) if all(x % y != 0 for y in range(2, int(x**.5) + 1))]
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

"""
Explanation:

1. range(2, int(x**0.5) + 1)
    This generates numbers to test as possible divisors of x:
    possible divisors for 36 are: (1, 36), (2, 18), (3, 12), (4, 9), (6, 6) 
    x**0.5: This calculates the square root of x.
    int(x**0.5) + 1: We take the integer part of the square root and add 1 to include the upper bound in the range.
    Why do we check up to the square root of x?

    If a number x is divisible by any number larger than its square root, it must also be divisible by a smaller number (e.g., for 36, if 36 is divisible by 9 which is larger than 6 "the square root", it’s also divisible by 4). Checking up to the square root is enough to determine primality.
    so 36 is divisible by 4 which is between 2, 7 , so 36 is not a prime number
2. x % y != 0
    This checks whether x is divisible by y:

    x % y: The modulo operator returns the remainder of x divided by y.
    x % y != 0: Means x is not divisible by y.
3. all(...)
    The all function returns True if all elements in the iterable are True.
    In this case:

    x % y != 0 for y in range(...) generates a sequence of True or False values for each y.
    If x is not divisible by any y in the range, all the conditions are True, and all() returns True.
    If x is divisible by any y, one of the conditions is False, and all() returns False.


"""

