"""
A decorator class is a way to use classes (instead of functions) to modify or extend the behavior of other functions or methods.

Understand What a Decorator Does
    A decorator is a tool in Python that wraps a function to modify or extend its behavior. Normally, decorators are written as functions, but you can also use classes to achieve the same.
For example, if you want to log every time a function is called, you can write a decorator.

Anatomy of a Decorator Class
    A decorator class works because Python allows objects of a class to behave like functions if the __call__ method is implemented. When you use a class as a decorator:

    The __init__ method is called when the decorator is applied.
    The __call__ method is invoked whenever the decorated function is called.
"""

# Example:
class MyDecorator:
    def __init__(self, func):
        # Store the decorated function in the instance
        self.func = func

    def __call__(self, *args, **kwds):
        # Add your decorator logic here
        print(f"Start calling function {self.func.__name__} with arguments: {args}, {kwds}")
        self.func(*args, **kwds)
        print(f"End calling function {self.func.__name__}")


@MyDecorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
"""
Explanation:
    What Happens in the Example?
        When @MyDecorator is applied:
            The MyDecorator class is instantiated with say_hello as its argument.
            The self.func in the class holds a reference to say_hello.
        When say_hello("Alice") is called:
            The __call__ method of MyDecorator is invoked.
            Inside __call__, we can add custom behavior (e.g., printing messages) before and after calling the original say_hello function.

output
    Start calling function say_hello with arguments: ('Alice',), {}
    Hello, Alice!
    End calling function say_hello
"""


# example: logging decorator
class LogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling function {self.func.__name__} with arguments: {args}, {kwargs}")
        result = self.func(*args, **kwargs)
        print(f"Finished function {self.func.__name__}, returned: {result}")
    

@LogDecorator
def add(x, y):
    return x + y

add(3, 5)
"""
output:
    Calling function add with arguments: (3, 5), {}
    Finished function add, returned: 8
"""


"""
When to Use a Decorator Class
    Stateful Decorators: When you need to maintain a state (e.g., count how many times a function is called).
    Complex Logic: When the decorator involves more logic than can be conveniently handled in a function.
"""

# Example: Stateful Decorator
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwds):
        self.count += 1
        name = self.func(*args, **kwds)
        print(f"Function {self.func.__name__} called {self.count} times")
        print(f"Hello, {name}!")

@CountCalls
def get_name(name):
    return name


get_name("Alice")
get_name("Bob")
get_name("John")
"""
output:
    Function get_name called 1 times
    Hello, Alice!
    Function get_name called 2 times
    Hello, Bob!
    Function get_name called 3 times
    Hello, John!
"""

"""
Advantages of Using a Decorator Class
    Organized Code: Easier to manage complex decorators compared to using functions.
    State Management: You can store persistent information (e.g., counters, configurations) inside the class.
"""

# Example : Conditional Execution Decorator
class ConditionalDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwds):
        # Provide default values if not explicitly passed
        # get values from the kwds with default values if no values provided and then no need to pass the default values in the function declaration
        # age = kwds.get('age', 29)  # Default age = 29
        # name = kwds.get('name', "Islam")  # Default name = "Islam"

        # Or call the original function to get `name` and `age` with the default name and age provided in the function declaration
        name, age = self.func(*args, **kwds)

        if age > 0:
            print(f"Hello, {name}!")
            print(f"Your age is {age}")
        else:
            print(f"Age should be positive!")


@ConditionalDecorator
def get_info(name="Islam", age=29):
    return name, age

get_info(name="Bob", age=39)  # Valid input
get_info(age=-5)             # Invalid age
get_info()                   # Uses default values
"""
Step-by-Step Breakdown

    1- Decorating the Function:

        When @ConditionalDecorator is applied to get_info:
            get_info = ConditionalDecorator(get_info)
        The get_info function is now replaced with an instance of ConditionalDecorator. This means calling get_info will trigger the __call__ method of ConditionalDecorator.

    2- Calling the Decorated Function:

        When you call get_info, Python automatically forwards all arguments (*args and **kwargs) to the __call__ method of ConditionalDecorator.
        For example:

            get_info(name="Bob", age=39)
        
            Internally:

            ConditionalDecorator.__call__(self, name="Bob", age=39)

    3- Forwarding Arguments to the Original Function:

        Inside the __call__ method, we call the original get_info function using:
        
            name, age = self.func(*args, **kwds)

        Here’s what happens:
            *args captures positional arguments as a tuple.
            **kwds captures keyword arguments as a dictionary.
            These are forwarded to the original get_info function.
        For example:
            name, age = get_info(name="Bob", age=39)
            The original function processes the arguments and returns the values

    4- Processing the Function’s Output:

        After the original function returns, the decorator class processes the returned values:
        
            if age > 0:
                print(f"Hello, {name}!")
                print(f"Your age is {age}")
            else:
                print(f"Age should be positive!")



output:
    Hello, Bob!
    Your age is 39
    Age should be positive!
    Hello, Islam!
    Your age is 29
"""



# example: Timer decorator
import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {self.func.__name__}: {end_time - start_time:.4f} seconds")
        return result

@Timer
def slow_function():
    time.sleep(1)  # Simulates a slow function
    print("Finished slow function")

slow_function()
"""
output:
    Finished slow function
    Execution time of slow_function: 1.0002 seconds - "the 1 seconds for the sleeping time"
"""


#----------------------------------------------------------------


# Example : Decorating Methods in a Class
class MethodLogger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling method {self.func.__name__} with arguments: {args}, {kwargs}")
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):
        # This binds the method to the instance (`calc`) automatically
        return lambda *args, **kwargs: self(instance, *args, **kwargs)


class Calculator:
    @MethodLogger
    def add(self, x, y):
        return x + y
    # This is equivalent to:
    # def add(self, x, y):
    #     return x + y
    # add = MethodLogger(add)  # 'add' is now wrapped by MethodLogger, acting as a non-data descriptor.


calc = Calculator()

# Now, Python knows to pass `calc` automatically to `add`:
result = calc.add(4, 5)  # Calling method add with arguments: (<Calculator object>, 4, 5), {}
print(result)  # 9


"""
Explanation:

    Simplified Analogy
        Imagine the Calculator is a car 🚗, and the add method is the steering wheel.
        When you decorate add, you remove the steering wheel and put a fancy cover on it (MethodLogger), but now the steering wheel isn't attached to the car anymore!
        The __get__ method re-attaches the wheel so you can actually steer the car.

    📦 What Happens When You Use a Class Decorator?
        @MethodLogger
        def add(self, a, b):
            return a + b

        is the same as 

        def add(self, a, b):
            return a + b

        add = MethodLogger(add)

        ✔ Meaning:
            The add method is wrapped by an instance of MethodLogger.
            So, add is no longer a function; it's now an object of MethodLogger.

    🔄 Why __call__ Is Used
        When you call:
            calc.add(3, 4)
        You're actually calling:
            MethodLogger(add).__call__(3, 4)


    Problem:
        Python doesn’t automatically pass self (the instance of Calculator) to the add method because add is now a regular object, not a bound method.
        

    🔑 What Does "Bind" Mean?
        Binding means connecting a method to the object (calc) so Python can automatically pass self.
            In regular methods, Python automatically binds the method to the object
                calc.add(3, 4)  # Python passes `calc` as `self`

            But decorators break this binding because add is now a MethodLogger object, not a method.

    🛠 Why We Need __get__
        By implementing __get__, we restore the binding.
            def __get__(self, instance, owner):
                return lambda *args, **kwargs: self(instance, *args, **kwargs)

         Explanation:
            instance: This is the object (calc) that owns the method.
            self: This is the MethodLogger instance wrapping the method.
        🔑 How It Works:
            When you call calc.add(3, 4), Python first checks if add has a __get__ method.
            __get__ binds the method to calc by returning a lambda that manually passes calc (instance) into the decorator.execute
            When binding is done, Python will execute the call method.

            
🚀 Summary
    MethodLogger is a non-data descriptor because it only has __get__.
    Decorating add with @MethodLogger replaces it with a MethodLogger(add) object.
    Python calls __get__ to bind the calc instance to the method.
    The lambda in __get__ ensures that calc is passed to __call__.
    __call__ then runs the original add method with the correct self and arguments.
"""
