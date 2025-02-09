"""
Decorators in Python
A decorator in Python is a powerful and elegant tool to modify or extend the behavior of functions or methods without altering their actual code. Decorators are often used for logging, authentication, input validation, and more.

Key Concepts
Functions are First-Class Objects:
In Python, functions can be passed as arguments, returned from other functions, and assigned to variables. This makes decorators possible.

Higher-Order Functions:
A function that takes another function as input or returns a function as output is called a higher-order function.

Closures:
A closure is a function object that remembers values in its enclosing scopes even if those scopes are no longer active. Decorators often use closures.

Syntax

    @decorator_name
    def my_function():
        pass

    this is equivalent to

    def my_function():
        pass
        
    my_function = decorator_name(my_function)

"""

# example

def greet_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper

@greet_decorator
def say_name():
    print("My name is Python.")

say_name()

"""
explanation:
    greet_decorator is a decorator function.
    It takes say_name as input and returns a wrapper function.
    The wrapper function adds behavior (printing "Hello!" and "Goodbye!") around the call to say_name.
"""

"""
output:
    Hello!
    My name is Python.
    Goodbye!
"""


# example
# Define a decorator
def introduce_yourself(func):
    def uppercase():
        name = func()  # Call the original function
        print(f"My name is {name.upper()}.")  # Convert the result to uppercase and print
    return uppercase  # Return the inner function

# Using the closure way
def get_name():
    return "John Doe"

uppercase = introduce_yourself(get_name)  # Decorate get_name using a closure
uppercase()  # Call the decorated function
# Output: My name is JOHN DOE.

# Using the decorator syntax (same result as above)
@introduce_yourself  # Decorate get_name directly
def get_name():
    return "John Doe"

get_name()  # Call the decorated function
# Output: My name is JOHN DOE.


#----------------------------------------------------------------

"""
Chaining Decorators
You can apply multiple decorators to a single function.
"""

def uppercasingMessage(func):
    def wrapper():
        return func().upper()  # here we just uppering the characters before pass it to the exclamation decorator then print the full message there
    return wrapper

def addExclamation(func):
    def wrapper():
        print(f"{func()}!")  # printing only in this step because it's the last step
    return wrapper

@addExclamation  # this executes second
@uppercasingMessage  # this executes first
def sayHello():
    return "Hello, World"

sayHello()  # HELLO, WORLD!


# example

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result}!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet(name):  # name here is represented by *args in the wrapper function
    return f"hello, {name}"

print(greet("ahmed"))  # HELLO, AHMED!


@exclamation_decorator
@uppercase_decorator
def greet(name="Ahmed", age=29):  # name, age here are represented by **kwargs in the wrapper function
    return f"hello, {name}, your age is {age}"

print(greet())  # HELLO, AHMED, YOUR AGE IS 29!
print(greet(name="islam", age=30))  # HELLO, ISLAM, YOUR AGE IS 30!. name and age here override the values on the function declaration
"""
Explanation:
    The uppercase_decorator converts the result to uppercase.
    The exclamation_decorator adds an exclamation mark.
    Decorators are applied from bottom to top, so uppercase_decorator runs first.
"""
"""
*args:
    Captures all positional arguments passed to the function.
    It's a tuple that holds all the extra positional arguments.

**kwargs:
    Captures all keyword arguments passed to the function.
    It's a dictionary that holds all the extra key-value pairs.
"""

#----------------------------------------------------------------

"""
Decorators are a type of higher-order function because they operate on functions and often return another function. Let’s clarify this with the characteristics:

What Is a Higher-Order Function?
    A function is called a higher-order function if it:

    Takes a function as an argument, or
    Returns a function as its result, or
    Does both (which decorators often do).

Why Are Decorators Higher-Order Functions?
    Decorators Take a Function:
    A decorator is applied to another function (or class), which it wraps or enhances.

    Decorators Return a Function:
    After wrapping, the decorator usually returns the new or modified function.
"""

# example:
def log_decorator(func):  # Takes a function as input
    def wrapper(*args, **kwargs):  # Inner function
        print(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)  # Calls the original function
        print(f"{func.__name__} returned {result}")
        return result  # Returns the result of the original function
    return wrapper  # Returns the inner function

"""
the decorator here
    Takes a function:
        func is the function being decorated.
    Returns a function:
        log_decorator returns the wrapper function, which is the enhanced version of the original function.    
"""

@log_decorator
def add(a, b):
    return a + b

"""
The decorator log_decorator wraps the add function:
    add is passed to log_decorator as func.
    log_decorator returns the wrapper function.
    Now, add is replaced with the wrapper.
When you call add(3, 5):
    The wrapper function is executed instead.
    Inside wrapper, the original add is called.
"""

#----------------------------------------------------------------

"""
Decorator Factory: What and Why?
    A decorator factory is a function that:
        Takes some arguments.
        Returns a decorator (which is itself a function).
    This pattern is used when you want to parameterize a decorator (i.e., pass arguments to it). In your example, the repeat_decorator function is a factory that produces a decorator.
"""
# example:
def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_decorator(3)
def greet(name):
    print(f"Hello, {name}!")

greet("John")
"""
output:
Hello, John!
Hello, John!
Hello, John!
"""

"""
Explanation:

    repeat_decorator (Decorator Factory):
        Takes the parameter times.
        Returns the actual decorator, decorator function.
    decorator (Actual Decorator):
        Takes a function func as its argument.
        Returns a wrapper function that wraps the behavior of func.
    wrapper (Inner Function):
        Adds the actual behavior (in this case, calling the function multiple times).
"""
"""
Notes:

    - You need this two-layered structure when you want the decorator to accept arguments.
    - Why Not Pass times Directly to the Decorator?
        Passing times directly to the decorator won’t work as intended because decorators are designed to take a function as their sole argument. If you directly pass times to a decorator, Python will get confused because it’s expecting a function, not an integer (or any other argument type).
"""