# lambda "b is silent"
# A lambda function in Python is a short, anonymous function defined using the lambda keyword. It's often used when you need a simple function for a short period of time.

# Syntx: lambda arguments:expression
# lambda: Keyword to define a lambda function.
# arguments: Input parameters (can be none, one, or multiple).
# expression: A single expression whose result is returned.

add = lambda x, y : x * y
# def add(x, y): return x + y # we replaced the def keyword with lambda, removed the function name so lambda is anonymous functino the removed the return keyword, so actually it's the same .
print(add(2, 3))

# Key Points:
# Lambda functions can have multiple arguments but only one expression.
# They're commonly used as short, throwaway functions, especially with higher-order functions.


#----------------------------------------------------------------


# Higher-Order Functions
# A higher-order function is a function that:
# Takes one or more functions as arguments, or
# Returns a function as its result.
# Python has built-in higher-order functions like map(), filter(), and reduce() that pair well with lambda functions.


# map() function
# The map() function applies a function to each item in an iterable (like a list) and returns a new iterable.
# Syntax: map(function, iterable)
myList = [1, 2, 3, 4]
squareMyList = list(map(lambda x: x * x, myList))
print(squareMyList) # [1, 4, 9, 16]


# filter() function
# The filter() function filters items from an iterable based on a condition defined in the function.
# Syntax: filter(function, iterable)
evenNumbers = list(filter(lambda x : x % 2 == 0, myList))
print(evenNumbers) # [2, 4]


# reduce() function
# The reduce() function from the functools module applies a function cumulatively "بشكل متكرر" to items in an iterable, reducing it to a single value.
# Syntax: reduce(function, iterable)
from functools import reduce
product = reduce(lambda x, y : x * y, myList)
print(product) # 24


# Examples:

# Convert a list of temperatures from Celsius to Fahrenheit:
temperatures = [0, 20, 30, 40]
fehrenheit = list(map(lambda c: (c * 9/5) + 32, temperatures))
print(fehrenheit) # [32.0, 68.0, 86.6, 104.0]

# Filter strings that start with a specific letter:
words = ["apple", "banana", "cherry", "avocado"]
awords = list(filter(lambda x : x.startswith('a'), words))
print(list(awords)) # ['apple', 'avocado']

# Concatenate all strings in a list:
words = ['Python', 'is', 'fun']
sentence = reduce(lambda x, y : x + " " + y, words)
print(sentence) # Python is fun


# Notes
# When discussing closures, the outer function qualifies as a higher-order function because it returns the inner function as a result.

# difference between higher order function and closure function
"""
Higher-Order Functions
A higher-order function is any function that:

Takes another function as an argument, or
Returns a function.

# Higher-order function taking a function as an argument
def apply_twice(func, x):
    return func(func(x))

# Higher-order function returning a function
def make_multiplier(n):
    def multiplier(x):
        return n * x
    return multiplier

"""
"""
What is a Closure?
A closure is a function that has access to variables from its enclosing scope even after the outer function has finished executing.

def make_counter():
    count = 0  # Free variable

    def counter():
        nonlocal count
        count += 1
        return count

    return counter

counter = make_counter()
print(counter())  # Output: 1
print(counter())  # Output: 2

Here, counter is a closure because it retains access to the variable count from the enclosing make_counter function, even after make_counter has exited.
"""

"""
Why Aren’t All Higher-Order Functions Closures?

A higher-order function may not always create a closure because it doesn't always "capture" variables from the enclosing scope. It might:

- Simply return a lambda or function that doesn’t depend on any free variables.
def make_adder():
    return lambda x: x + 1

adder = make_adder()
print(adder(10))  # Output: 11


- Take a function as an argument without creating a new function that depends on an outer variable.
def apply_function(func, x):
    return func(x)

result = apply_function(lambda y: y ** 2, 5)
print(result)  # Output: 25
Here, apply_function is a higher-order function, but it does not create a closure because no variables are captured from an outer scope.

"""

"""
but we might have a lambda that is a closure
def multiplier(n):
    return lambda x: x*n


print(multiplier(2)(5))  # Output: 10
or
multiplier = multiplier(2)
print(multiplier(5)) # Output: 10
"""

# in the below example, multiplier is a higher-order function because it returns multiply_by.
# The returned multiply_by function is a closure because it retains the value of factor from the environment of multiplier.
def multiplier(factor):  # Outer function (higher-order function)
    def multiply_by(value):  # Inner function (closure)
        return factor * value  # Uses the variable `factor` from the outer function
    return multiply_by  # Returning the inner function

double = multiplier(2)  # Create a closure with factor = 2
triple = multiplier(3)  # Create a closure with factor = 3

print(double(5))  # Output: 10 (2 * 5)
print(triple(5))  # Output: 15 (3 * 5)


# In closures, the outer function is indeed a higher-order function because it returns the inner function.
# Closures add the unique property of the inner function "remembering" variables from the outer function’s scope, making it context-aware.
# The concept of a higher-order function or a closure applies regardless of whether the returned function is a lambda or a regular function. The key is that the outer function returns a callable function.


# another example:
from functools import reduce

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)
print(sum(numbers, 10))

# Explanation:
# reduce is a function from the functools module that applies a binary function (in this case, the lambda) cumulatively to the items in an iterable, reducing it to a single value.

# Lambda function: lambda acc, curr: acc + curr
# This is a simple lambda function that adds two numbers (acc and curr).
# acc stands for accumulator "تراكم", and curr stands for current value in the iterable.
# Iterable (numbers): [1, 2, 3, 4, 5, 1]

# This is the list of numbers that we will process.
# Initial value (10): The third argument to reduce is the initial value of the accumulator (acc). It will start with the value 10.

# How It Works:
# reduce will apply the lambda function cumulatively across the elements of the list.
# The process:
# Start with the initial value (10):
# acc = 10, curr = 1: acc + curr = 10 + 1 = 11
# Next element (2):
# acc = 11, curr = 2: acc + curr = 11 + 2 = 13
# Next element (3):
# acc = 13, curr = 3: acc + curr = 13 + 3 = 16
# Next element (4):
# acc = 16, curr = 4: acc + curr = 16 + 4 = 20
# Next element (5):
# acc = 20, curr = 5: acc + curr = 20 + 5 = 25
# Next element (1):
# acc = 25, curr = 1: acc + curr = 25 + 1 = 26
# The final result after applying the lambda to all elements is 26.
# Output:
# 26
# print(sum(numbers, 10))
# Explanation:
# The sum function takes two arguments:
# The iterable (numbers): [1, 2, 3, 4, 5, 1]
# The initial value (10): This is the value from which the sum will start.
# The sum function will add all elements in the iterable (numbers) to the initial value (10).
# How It Works:
# The sum function will start with the initial value of 10 and add each element in the list to it.
# 10 + 1 = 11
# 11 + 2 = 13
# 13 + 3 = 16
# 16 + 4 = 20
# 20 + 5 = 25
# 25 + 1 = 26
# Output:
# 26


# another example:

names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)

# Explanation:
# The goal of this example is to count the total number of characters in all the names.

# The lambda function: lambda acc, curr: acc + len(curr)

# acc is the running total of character counts.
# curr is the current name in the list.
# len(curr) calculates the number of characters in each name.
# The initial value: 0

# We start counting from 0.
# How It Works:
# reduce will process the list of names and sum up the length of each name.
# Initial value = 0:
# acc = 0, curr = "Dave Gray": acc + len(curr) = 0 + 9 = 9 (9 characters in "Dave Gray")
# acc = 9, curr = "Sara Ito": acc + len(curr) = 9 + 8 = 17 (8 characters in "Sara Ito")
# acc = 17, curr = "John Jacob Jingleheimerschmidt": acc + len(curr) = 17 + 31 = 48 (31 characters in "John Jacob Jingleheimerschmidt")
# output
#48


# reduce function:
# It allows for more complex accumulation or transformations and can apply a function cumulatively over an iterable. It provides more flexibility because you can define your own function logic (like the lambda function) for how you accumulate or modify values.

# sum function:
# It is a simpler and more specific function for adding up values. It’s easy to use when you only want to sum a list of numbers, optionally starting with an initial value.

print(sum([1, 2, 3], 4)) # we start from 4, 4 + 1 = 5 + 2 = 7 + 3 = 10

#----------------------------------------------------------------

def add(x, y):
    return x + y

multiplier = lambda x, y: x* y

def subtract(x, y):
    return x - y

division = lambda x, y: x/y if y !=0 else "can't divide by 0"

def operation(function, x, y):
    return function(x, y)

print(operation(add, 3, 4)) # Output: 7
print(operation(multiplier, 3, 4)) # Output: 12
print(operation(subtract, 3, 4)) # Output: -1
print(operation(division, 3, 0)) # Output: "can't divide by 0"
print(int(operation(division, 3, 1))) #  Output: 3


#----------------------------------------------------------------


# Nested Functions
# The use of a nested function (say) keeps the logic for printing words encapsulated within split_phrase.
def split_phrase(phrase):
    count = 0
    def say(word):
        nonlocal count
        count += 1
        print(str(count) +". " + word)

    for word in phrase.split(): # use split() function to split phrase to list of words otherwise it will split it to list of characters
        say(word)

phrase = "Ahmed always goes to school"
split_phrase(phrase)
# output:
"""
1. Ahmed
2. always
3. goes
4. to
5. school
"""

# same function but with reduce
result = reduce(
    lambda acc, word_tuple: f"{acc}\n{word_tuple[0] + 1}. {word_tuple[1]}",  # Lambda function to build the string
    enumerate(phrase.split()),  # `enumerate` provides (index, word) pairs from the split phrase
    ""  # Initial value for the accumulator (an empty string)
)

# `strip` removes the leading and trailing newlines added during the reduction process
print(result.strip())

#output:
"""
1. Ahmed
2. always
3. goes
4. to
5. school
"""


"""
reduce always needs an accumulator "acc" to track the intermediate results. The accumulator is either provided explicitly (through the initial argument) or implicitly starts as the first element of the iterable.

Without an accumulator, reduce would not know how to combine the results across iterationsand will produce an error .

if the iterable is empty, there's no first element to use as the accumulator and no initial value, this leads to an error.

This will raise an error because there's no element to start the accumulation
numbers = []
result = reduce(lambda acc, x: acc + x, numbers)

unless we added 0 as an initial value
numbers = []
result = reduce(lambda acc, x: acc + x, numbers, 0)
"""