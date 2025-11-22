"""
Duck Typing is a concept derived from the saying:

"If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

In programming, this means an object’s type doesn’t matter as long as it behaves like the expected type. Instead of focusing on what class the object belongs to, Python checks if the object has the required methods or attributes to perform an action.

Key Idea of Duck Typing
    Python is a dynamically-typed language. This means you don’t need to specify an object's type explicitly.
    You can focus on what the object can do (methods/attributes) rather than its specific type.
"""

# Simple Example 1: Duck Typing with a Function
# Imagine we have a function that expects an object that can "quack."
def make_it_quack(duck):
    duck.quack()

class Duck:
    def quack(self):
        print("Quack! Quack!")

class Person:
    def quack(self):
        print("I can quack like a duck!")

# Example usage
donald = Duck()
john = Person()

make_it_quack(donald)  # Output: Quack! Quack!
make_it_quack(john)    # Output: I can quack like a duck!
"""
In this example:

    The function doesn’t care about the type of duck.
    As long as the object passed has a quack method, the function works. Both Duck and Person can be used.
"""


# Example 2: File-like Objects
# Consider a function that reads data from objects that behave like files (they have a read method).
def read_file(file_obj):
    return file_obj.read()

class RealFile:
    def read(self):
        return "Reading from a real file!"

class FakeFile:
    def read(self):
        return "Simulating file reading!"

# Example usage
real_file = RealFile()
fake_file = FakeFile()

print(read_file(real_file))  # Output: Reading from a real file!
print(read_file(fake_file))  # Output: Simulating file reading!
"""
Here:
    read_file doesn’t check if the object is actually a file.
    It only expects the object to have a read method.
"""


# Example 3: Polymorphism with Duck Typing
# You might have multiple classes with a speak method:
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep Boop!"

def animal_sounds(animal):
    print(animal.speak())

# Example usage
dog = Dog()
cat = Cat()
robot = Robot()

animal_sounds(dog)    # Output: Woof!
animal_sounds(cat)    # Output: Meow!
animal_sounds(robot)  # Output: Beep Boop!


# Example 4: Using Duck Typing with Iterables
# You can use Duck Typing to work with objects that behave like lists or other iterables.
def iterate_over(data):
    for item in data:
        print(item)

# Example usage
list_data = [1, 2, 3]
tuple_data = (4, 5, 6)
set_data = {7, 8, 9}

iterate_over(list_data)  # Output: 1 2 3
iterate_over(tuple_data) # Output: 4 5 6
iterate_over(set_data)   # Output: 7 8 9
"""
Here:

    The function doesn’t care if the object is a list, tuple, or set.
    It only checks if the object is iterable (i.e., you can loop through it).
"""


"""
Advantages of Duck Typing
    Flexibility: You can work with objects of different types, as long as they have the required behavior.
    Code Reusability: Functions can handle different objects without being tightly coupled to specific classes.
    Simplicity: Focus on what the object can do instead of its specific type.

Disadvantages of Duck Typing
    Runtime Errors: If an object doesn’t have the required method or attribute, it will fail at runtime.
    Harder Debugging: Debugging may become challenging if incorrect objects are passed to a function.
"""


# Example of Error with Duck Typing
# If an object doesn’t have the required method, Python raises an AttributeError.
class Car:
    def drive(self):
        print("Driving!")

# Example usage
car = Car()

try:
    make_it_quack(car)  # The `Car` object doesn't have a `quack` method
except AttributeError as e:
    print(f"Error: {e}")  # Error: 'Car' object has no attribute 'quack'


"""
Why is Duck Typing Important?
    1. Focus on Behavior, Not Type
        In Python, what an object can do is often more important than what it is. This makes your code less restrictive and more general.
        You don’t need to write separate code for each specific type, as long as the types share the required behavior.

        Example:
        Imagine you are writing a logging function. You don’t care if the object is a file, a socket, or a database connection—you just want it to have a write method.

            def log_message(writer, message):
                writer.write(message)

            # Works with different types of objects
            class FileLogger:
                def write(self, message):
                    print(f"Logging to a file: {message}")

            class ConsoleLogger:
                def write(self, message):
                    print(f"Logging to console: {message}")

            log_message(FileLogger(), "Hello, File!")
            log_message(ConsoleLogger(), "Hello, Console!")
            This function works with any object that has a write method—no need to hardcode for specific classes.

    2. Reduces Code Duplication
        Without Duck Typing, you might write multiple versions of the same function to handle different types.
        With Duck Typing, one function can handle many types as long as they have the required behavior.

        Example:
        You want a function to iterate over items, whether they come from a list, set, or database cursor.
            def print_items(data):
                for item in data:
                    print(item)

            # Works with lists, sets, and even custom objects with similar behavior
            print_items([1, 2, 3])       # Works with lists
            print_items({4, 5, 6})       # Works with sets

            
    3. Polymorphism without Inheritance
        In traditional object-oriented programming (OOP), polymorphism (using objects of different classes interchangeably) is often achieved through inheritance.
        Duck Typing allows polymorphism without requiring a shared base class.
        Example:
        Different objects can implement their own render method, and you can treat them the same without enforcing a common base class.
            class HTMLButton:
                def render(self):
                    return "<button>Click Me!</button>"

            class TextField:
                def render(self):
                    return "<input type='text' />"

            def render_component(component):
                print(component.render())

            render_component(HTMLButton())  # Output: <button>Click Me!</button>
            render_component(TextField())  # Output: <input type='text' />
            No need to define a common parent class like UIComponent. The function just expects the render method.

    4. Supports Python’s Dynamic Nature
        Python is dynamic, meaning you don’t need to explicitly declare types.
        Duck Typing aligns perfectly with Python’s philosophy: "We’re all adults here." You trust objects to have the required behavior.

"""


"""
The term "interface" does have different meanings in different contexts. Let's break down its meaning, especially in the context of Duck Typing and abstraction, to clear things up.

What Does "Interface" Mean?
In General Programming: An interface is a set of methods or behaviors that an object must provide. It’s a contract that guarantees the object can perform certain actions, but it doesn't specify how those actions are implemented.

In the Context of Duck Typing: In Duck Typing, an "interface" doesn't necessarily mean a formal class with declared methods. Instead, it's just the set of methods or properties that an object is expected to have to work with a function or another object.

Example:
    When we say an object satisfies the "expected interface" in Duck Typing, we mean the object behaves in a certain way, like having specific methods or attributes. The object doesn't need to formally declare that it implements a certain "interface" (as in statically-typed languages), but it just needs to have the required behavior.

For instance:
    If you pass an object to a function that expects it to be "iterable," the function doesn’t care if the object is a list, a tuple, or a custom class. All that matters is that the object can be iterated over, meaning it implements the __iter__ method.
    This is the "interface" in the context of Duck Typing: the object must provide the __iter__ method (the behavior), not necessarily inherit from a specific class.

Example in Duck Typing:
    def make_it_speak(animal):
        animal.speak()

    class Dog:
        def speak(self):
            print("Woof!")

    class Cat:
        def speak(self):
            print("Meow!")

    make_it_speak(Dog())  # Output: Woof!
    make_it_speak(Cat())  # Output: Meow!
    Here, Dog and Cat both provide the speak method. The make_it_speak function expects an object with a speak method, and it works with both Dog and Cat without worrying about their actual types. The objects implement the expected behavior (the interface) without being formally declared as implementing any interface.

In conclusion:
    Interface in Duck Typing: A set of methods or behaviors an object must have (informal).
    Interface in OOP/Abstraction: A formal declaration of methods that must be implemented by a class.
"""