"""
*args

Used in a function definition to accept a variable number of positional arguments "unknown numbers of arguments".
It collects the arguments into a tuple.
Useful when you don’t know beforehand how many arguments will be passed to the function.
"""

def sumOfNumbers(*nums):
    return sum(nums)

print(sumOfNumbers(1, 2, 3, 4, 5))  # Outputs: 15




"""
**kwargs

Used in a function definition to accept a variable number of keyword arguments.
It collects the arguments into a dictionary.
Useful when you want to handle named arguments dynamically.

"""

def techCompanies(**companies):
    for key, value in companies.items():
        print(f"{key} uses {value}")

techCompanies(facebook = "PHP", twitter = "PHP", Google = "Python") # multiple key/value pairs




# Unpacking Operators (* and **)

"""
Single * (Unpacks iterables)

The * operator can unpack elements from any iterable (e.g., list, tuple, set).
Typically used in function calls or assignments.
"""

# numbers = [1, 2, 3, 4]
numbers = (1, 2, 3, 4)
print(*numbers) # 1 2 3 4 

a, *b, c = [1, 2, 3, 4]
print(a)  # 1
print(b)  # [2, 3]
print(c)  # 4



"""
Double ** (Unpacks dictionaries)

The ** operator unpacks key-value pairs from a dictionary.
Typically used in function calls.
"""

persondata1 = {"name": "John", "age": 26}
persondata2 = {"job": "programmer", "status": "married"}
persondata = {**persondata1, **persondata2}
print(persondata)


# Unpacking in function calls
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(**persondata1)



# Combining both args and kwargs

def combine(*args, **kwargs):
    print(f"This is args: {args}")
    print(f"This is kwargs: {kwargs}")


combine(1, 2, 3, name="John", age=26) # This is args: (1, 2, 3) \n This is kwargs: {'name': 'John', 'age': 26}



# Notes
# You cannot use **kwargs to unpack a dictionary directly into variables like you can with a list or tuple, but you can unpack them in the function call like the above example of the greet function

# name, age = persondata  # this will produce an error 
name, age = persondata1["name"], persondata1["age"]  # this works fine
name, age = persondata1.values() # this also works fine, but assumes the order of values matches your variable expectations.