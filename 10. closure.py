# A closure is when a function remembers the variables from the place where it was created, even after that place (the outer function) is finished.
# This means the inner function can use values from the outer function, even when the outer function is no longer running.

# def defList(*numbers):
#     print(type(list(numbers)), list(numbers))

# defList(1, 2, 3)
# exit()
def outer_function(value):
    def inner_function(inner_value):
        print("the inner value is: {inner_value}, the outer value is: {value}".format(inner_value=inner_value, value=value))
    return inner_function

# Create an instance of the outer function
outer_instance = outer_function(20)

# Call the inner function with a different value
outer_instance(30)  # the inner value is: 30, the outer value is: 20

# Explanation:
# outer_function has a variable value and a nested function inner_function.
# outer_function finishes running but returns the inner_function.
# The returned inner_function still remembers value (20) even though outer_function is done.

#----------------------------------------------------------------

def counter_function():
    count = 0
    def increment(value):
        nonlocal count  # Using nonlocal keyword to access the outer function's variable count
        while count <= value:
            print(count)
            count += 1

    return increment

counter = counter_function()
counter(10)

#  output:
# 0
# 1
# 2
# .
# .
# 10


# Explanation:
# Outer Function (counter_function):
# It initializes count to 0.
# It defines an inner function increment that can access and modify count.

# Inner Function (increment):
# It accepts a parameter value.
# It uses the nonlocal keyword to access and modify the count variable from the outer function.
# It runs a while loop that prints numbers starting from count (initially 0) until it reaches value.

# Returning the Inner Function:
# The counter_function function returns the increment function. This creates a closure where increment remembers the count variable, even after counter_function has finished executing.

# Calling the Closure:
# The line counter = counter_function() creates the closure.
# The call counter(10) executes the increment function, printing numbers from 0 to 10.

# Nonlocal Keyword:
# nonlocal count allows the increment function to modify the count variable from the outer function (counter_function), instead of creating a new local variable with the same name.

# Closure:
# When counter = counter_function() is called, a closure is created. The increment function keeps a reference to the count variable, even though the counter function has already finished executing.

# Reusing the Counter
# If you call counter(25) again, it will continue from where it left off. For example:
counter(25)

# Output:
# 11
# 12
# .
# .
# .
# 25

# Why This Code Is Ideal:

# Encapsulation:
# The count variable is private to the closure, ensuring that its state is maintained across calls to increment.

# Nonlocal Access:
# The nonlocal keyword allows increment to modify the count variable from the enclosing counter function.

# Reusability:
# You can create multiple independent counters by calling counter_function() again.
new_counter = counter_function()
new_counter(5)

# Output:
# 0
# 1
# 2
# 3
# 4
# 5

# ----------------------------------------------------------------

def outer_muliply(num1):
    def inner_multiply(num2):
        # we don't need to use nolocal with num1 if we will not modify it
        # nonlocal num1
        # num1 += 2
        return num1 * num2
    return inner_multiply

multiply_2_by_5 = outer_muliply(2)
print(multiply_2_by_5(5))  # 10

multiply_5_by_5 = outer_muliply(5)
print(multiply_5_by_5(5))  # 20


# note
# return increment: You're returning the function object itself (the reference to the function), so no parentheses.
# return increment(): This would call the function and return the result of the call, which is not what you want here because you’re working with a closure and want to return the function for later use.



# Example:
# Define a function to encapsulate and manage the `charlist`
# Practicing recursion & closure
def define_list(charlist):
    # Keep a copy of the original charlist to allow resetting later
    charlist_copy = charlist.copy()
    
    # Inner function to recursively build a word
    def make_word():
        nonlocal charlist  # Allows modifying the `charlist` in the enclosing scope
        if len(charlist) == 0:  # Base case: If the list is empty
            return '.'  # Return a period as the end of the word
        # Pop the first character, concatenate it, and recursively process the rest
        return charlist.pop(0) + make_word()
    
    # Inner function to reset the charlist to its original state
    def reset_charlist():
        nonlocal charlist  # Allows modifying the `charlist` in the enclosing scope
        # Reset `charlist` to a new copy of the original list
        charlist = charlist_copy.copy()
        return charlist  # Return the reset list for confirmation
    
    # Return both inner functions for external use
    return make_word, reset_charlist


# Example usage:

# Initial character list
charlist = ['T', 'h', 'a', 'n', 'k', ' ', 'y', 'o', 'u']

# Create the closure with `make_word` and `reset_charlist`
make_word, reset_charlist = define_list(charlist)

# Call `make_word` to process the characters and build a word
print(make_word())  # Outputs: "Thank you."

# Call `reset_charlist` to reset `charlist` to its original state
print(reset_charlist())  # Outputs: ['T', 'h', 'a', 'n', 'k', ' ', 'y', 'o', 'u']

# Call `make_word` again after resetting
print(make_word())  # Outputs: "Thank you."



# Example

def math_oper(operation_type):
    def operation(*numbers): # we deal with numbers here inside the function as a tuple
        if not numbers:
            print("No numbers provided")
            return 
        
        if not all(isinstance(n, (int, float)) for n in numbers):
            print("All arguments should be numbers")
            return
        
        # operation_type.__name__ to get the name of the function
        operation_name = getattr(operation_type, __name__, 'Unknown operation')
        # there are situations where the function passed as an argument might not have a __name__ attribute, and this typically occurs when you're working with anonymous functions, such as those created using lambda.
        print(f"This is {operation_name} operation and it's result is {operation_type(*numbers)}")

    return operation

def add(*numbers):
    return sum(numbers)

def multiply(*numbers):
    if len(numbers) == 0:
        return 1
    
    return numbers[0] * multiply(*numbers[1:]) # used * in *numbers[1:] because multiply function expects separate arguments, not a single collection, and this is a recursive function btw

math_operation = math_oper(add)
math_operation(1, 2, 3) # 1 + 2 + 3 = 6, the arguments here should be separated not a tuple as we deal with it inside the function

math_operation = math_oper(multiply)
math_operation(1, 2, 3, 4) # 1 * 2 * 3 * 4 = 6, the arguments here should be separated not a tuple as we deal with it inside the function
