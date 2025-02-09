count = 1   # Global variable

def another():
    color = "blue"  # # Enclosing scope variable
    global count # Access the global variable
    count += 1 # modify the global variable
    def greeting(name): # we can define a function inside another function, but using it locally " inside the parent function like local variable", nested function
        nonlocal color # use nonlocal keyword to access the enclosing `color` variable
        color = "red"  # Modify the enclosing variable
        print(count)
        print("Hello {name}, Your fav color is {color}".format(name=name, color=color))

    greeting("Islam")  # call the nested function

another()


# 1. global Keyword
# The global keyword is used to access or modify variables declared in the global scope from within a function. Without global, a variable assignment inside a function creates a new local variable, even if a variable with the same name exists in the global scope.

# global count
# count += 1   # declare it then assign it in a separated line

# Here, global count tells Python that the count variable inside the function refers to the global variable count, not a new local variable.
# count += 1 modifies the global count variable (originally 1) by incrementing it.
# If you omitted global, Python would throw an error when trying to modify count, because the function would assume it's a local variable, and you cannot modify a variable before declaring it.


# 2. nonlocal Keyword
# The nonlocal keyword is used to access and modify variables in an enclosing (non-global) scope. It allows you to work with variables in the nearest enclosing function that is not global.

# nonlocal color
# color = "red"

# nonlocal color tells Python to use the color variable from the enclosing another() function, not create a new local variable inside greeting().
# This means the color variable defined in another() is modified when color = "red" is executed.
# If you omitted nonlocal, a new local variable named color would be created inside greeting(), leaving the color in another() unchanged.