def sum(num1, num2=0):  # num1, num2 are parameters of the function
    # In Python, parameters with default values must come after parameters without default values.
    if type(num1) is not int or type(num2) is not int:
        return  # this will return none word in case of one of the arguments is not integer
    return num1 + num2

total = sum(1, 2) # 1, 2 are arguments to the function
print(total)
# Parameters are part of the function definition, while arguments are part of the function call.


# Function with *args to accept multiple positional arguments
def names_list(*names):
    print(names)  # Print the tuple of arguments
    print(type(names))  # Print the type (tuple)

# Function with **kwargs to accept multiple keyword arguments
def full_name(**full_name):
    print(full_name)  # Print the dictionary of key-value pairs
    print(type(full_name))  # Print the type (dict)

# Tuples are passed as arguments using *args
names_list('John', 'Doe', 'Jane', 'Sue')

# Dictionaries are passed as keyword arguments using **kwargs
full_name(first_name='John', last_name='Doe')


#----------------------------------------------------------------

# First class functions

"""
In Python, first-class functions refer to the concept that functions are treated as first-class citizens.

This means that functions in Python can be:

1- Assigned to variables.
2- Passed as arguments to other functions.
3- Returned from other functions.
4- Stored in data structures like lists, dictionaries, etc.

This is a core feature of Python and allows for flexible and dynamic programming patterns.


Key Features of First-Class Functions:

1- Assignment: Functions can be assigned to variables.
2- Passing: Functions can be passed as arguments to other functions.
3- Returning: Functions can be returned from other functions.
4- Storing: Functions can be stored in collections like lists, tuples, dictionaries, etc.


so all functions are first-class citizens. This means that every function in Python, including built-in functions, user-defined functions, lambda functions, etc., can be assigned to variables, passed as arguments, returned from other functions, and stored in data structures.
"""


# 1. Assigning a function to a variable

def addition(x, y):
    return x + y

add = addition
print(add(1, 2))  # 3


# 2. Passing a function as an argument
def add_oper(addition, x, y):
    print(addition(x, y))

add_oper(addition, 1, 2)


# 3. Returning a function from a function
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_five = create_adder(5)
print(add_five(3))  # 8


# 4. Storing a function in a data structure
def subtract(x, y):
    return x - y

operations = [addition, subtract]
print(operations[0](2, 3))
print(operations[1](2, 3))

operations_dict = {
    'add': addition,
    'sub': subtract,
}

print(operations_dict['add'](2, 3))
print(operations_dict['sub'](2, 3))


"""
Why is this important?

The ability to treat functions as first-class citizens gives Python a great deal of flexibility and expressiveness. Some common use cases include:

- Higher-order functions: Functions that take other functions as arguments or return them.
- Functional programming techniques: Such as map, filter, and reduce.

What is "Functional Programming"?

    Functional programming is a programming style that focuses on:
        - Writing pure functions (no side effects)
        - Using functions as values (you can pass them, return them, etc.)
        - Emphasizing data transformation over changing data in place
    It’s different from the imperative style, which uses loops and variables to modify state step by step.

- Imperative style is the tradition way 
    EX:
        numbers = [1, 2, 3, 4]
        result = []
        for n in numbers:
            result.append(n * 2)
        print(result)  # [2, 4, 6, 8]

        
- Callbacks: Passing a function to another function to be executed later.

"""


people = ["Alice", "bob", "Charlie"]
sorted_list = sorted(people, key=str.lower)  
print(sorted_list)   # ['Alice', 'bob', 'Charlie']

# Uppercase letters (like 'A') come before lowercase (like 'b').
# But here you're passing key=str.lower as a callback, which means: "Before comparing items, convert them to lowercase."
# The key argument is used to transform each item before sorting.
# str.lower → pass the function itself not calling it.
# str.lower() → would raise an error (you can't call lower() on the class itself).
