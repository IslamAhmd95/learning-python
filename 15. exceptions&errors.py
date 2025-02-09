x = 2

try:
    # print(x)
    # print(x / 0)
    print(x.lower())
except NameError:
    print("NameError means some variable might be undefined") # in case of x is not defined
except ZeroDivisionError:
    print("Do not divide by zero") # in case of division by zero
except Exception as e:
    print(f"An unexpected error occurred: {e}") # in case of any other error, x.lower() case
else:
    print("This executed in case of no errors")
    print(f"result is {x}")
finally:
    print("This will always run, whether there's an error or not")


# Common python built-in exceptions -> https://www.w3schools.com/python/python_ref_exceptions.asp

#----------------------------------------------------------------

## Types of Errors in Python

# 1- Syntax Errors
# These occur when the code violates Python's grammar rules.
# They are detected during the parsing phase and prevent the program from running.

# 2- Runtime Errors
# These occur while the program is running.
# These include exceptions like dividing by zero or accessing an invalid index.

#----------------------------------------------------------------

##  Raising Exceptions
# You can raise exceptions manually using the raise keyword.

def withDraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient amount to draw")
    return balance - amount

try:
    withDraw(100, 200)
except ValueError as e:
    print(f"Error: {e}")


#----------------------------------------------------------------


## Custom Exceptions
# You can create your own exception classes by inheriting from Exception.

class negativeNumberError(Exception):
    pass

def square_root(number):
    if number < 0:
        raise negativeNumberError("Negative number cannot be used for square root")
    return number ** 0.5

try:
    print(square_root(-4))
except negativeNumberError as e:
    print(f"Error: {e}")

#Explanation:

# The if statement ensures the function validates input and raises an error. The try-except block allows the caller to handle the error gracefully, avoiding program crashes, terminating the execution of the program and providing a better user experience.

# You could skip the try-except block if you're okay with the program terminating upon encountering the error. However, in most real-world applications, handling exceptions is considered good practice.



# Example
y = 'test'

def printInt(y):
    if not type(y) is int:
        raise TypeError('Variable y must be an integer')

try:
    printInt(y)
except TypeError:
    print('Caught a TypeError')

print(y)  # this will execute because try except will not stop the program, but just raising the exception then continue execution. Without try except block, the program will stop executing on printInt(y) because of the raise statement .

#----------------------------------------------------------------

"""
If an exception is raised inside the try block, whether it's intentional "عن عمد" (raise) or unintentional, Python immediately checks if there is a matching except block.
    If a matching except block is found, it is executed.
    If no matching except block is found, the exception propagates further up the call stack and might crash the program.
"""
def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")  # Manually raise an exception, Python looks for a matching except block for ValueError.
    return f"Processing age: {age}"

try:
    process_age(-5)  # Invalid input
except ValueError as e:
    print(f"Error: {e}")
# output: Error: Age cannot be negative!



# An exception of a different type is raised:
try:
    raise KeyError("This is not a ValueError.")
except ValueError as e:
    print(f"Caught an exception: {e}")

"""
output:
Traceback (most recent call last):
  File "<file_name>", line 2, in <module>
    raise KeyError("This is not a ValueError.")
KeyError: 'This is not a ValueError.'
"""