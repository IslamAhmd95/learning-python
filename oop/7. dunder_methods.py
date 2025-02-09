"""
Dunder methods (short for Double UNDERscore), also called magic methods or special methods, are predefined methods in Python with double underscores at the beginning and end of their names, like __init__, __str__, and __add__. These methods allow customization of how objects behave with built-in operations and functions.

Key Features
    Customization: Dunder methods let you define custom behavior for operators (+, -, *) and built-in functions (len(), str()).
    Object Representation: Methods like __str__ and __repr__ define how objects are displayed.
    Object Lifecycle: Methods like __init__ and __del__ handle initialization and destruction.
    Comparison and Hashing: Methods like __eq__, __lt__, and __hash__ enable comparisons and dictionary key usage.

Overriding Default Behavior of Dunder Methods
    Yes, you can override the default behavior of any dunder method, including __repr__. You don’t need to adhere strictly to the default intent, but it’s best to follow conventions for clarity and maintainability.
"""

## Common dunder methods

# Object Initialization: __init__: Called automatically when an object is created.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
print(person.name, person.age)  # Output: Alice 30



# String Representation: __str__ and __repr__
# __str__: User-friendly representation of the object (e.g., print()).
# __repr__: Unambiguous representation, often used for debugging.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("Alice", 30)
print(person)  # Output: Person(Name: Alice, Age: 30)
print(repr(person))  # Output: Person('Alice', 30)



# Arithmetic Operations: __add__, __sub__, __mul__, etc.
# Customize the behavior of operators like +, -, and *.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: Point(4, 6)



# Comparison: __eq__, __lt__, __le__, etc.
# Define comparison logic for objects.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
print(p1 == p2)  # Output: False
print(p1 < p2)   # Output: False



# Length: __len__
# Define behavior for the len() function.
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["Alice", "Bob", "Charlie"])
print(len(team))  # Output: 3



# Indexing and Iteration: __getitem__, __setitem__, __iter__
# Customize object behavior for indexing and looping.
class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __iter__(self):
        return iter(self.items)

my_list = MyList([1, 2, 3])
print(my_list[0])  # Output: 1
my_list[1] = 42
print(my_list[1])  # Output: 42
for item in my_list:
    print(item)  # Output: 1, 42, 3



# Callable Objects: __call__
# Make an object behave like a function.
class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting}, {name}!"

greeter = Greeter("Hello")
print(greeter("Alice"))  # Output: Hello, Alice!



# Context Management: __enter__ and __exit__
# Enable objects to be used with the with statement.
class Resource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Releasing resource")

with Resource() as r:
    print("Using resource")
# Output:
# Acquiring resource
# Using resource
# Releasing resource



# Object Destruction: __del__
# Called when an object is about to be destroyed.
# the __del__ method does not explicitly delete the object. Instead, it serves as a "destructor" that gets called automatically when the object is about to be destroyed by the Python garbage collector.
class Example:
    def __del__(self):
        print("The object is being deleted")

    def __str__(self):
        return "This is the object"

obj = Example()
print(obj)  # Output: this is the object
ref = obj  # A new reference ref is created, pointing to the same object as obj. Now, there are two references to the same object: obj and ref.
del obj  # Output: The object is being deleted
print(ref)  # Output: This is the object
# print(obj) # NameError: name 'obj' is not defined

"""
When you use del obj, it removes the obj reference from the current namespace but does not delete the object itself because another reference (ref) still exists.

When del obj is called:
    Object Deletion: The obj is deleted from memory, assuming no other references to it exist.
    Method Call: Before the object is destroyed, Python invokes the __del__ method to perform cleanup or display messages.
    If obj still has references elsewhere, the __del__ method won't trigger, and the object won't be deleted.

Key Behavior:
    Reference Count: Python uses reference counting to manage objects. As long as there's at least one reference to an object, it will not be garbage collected.
    Deleting a Name: When you use del obj, you're deleting the name obj but not the underlying object itself if it has other references.
    Access via Other References: Since ref is still pointing to the object, you can access and use it.

When Does __del__ Run?
    The __del__ method will only be triggered when the last reference to the object is removed, and the object is garbage collected:

    del ref  # Now the object has no references, and __del__ is called

    
Here's what happens step by step:
    del obj Statement:
        The del obj statement reduces the reference count of obj by one.
        If the reference count of the object reaches zero (no other references exist), the garbage collector will destroy the object.
        Before destruction, Python will automatically invoke the __del__ method (if defined).
    Printing the Message:
        Inside the __del__ method, any code you include (like print) will execute. This is useful for cleanup tasks, logging, or confirmation of deletion.
    Object Deletion:
        After the __del__ method runs, the object is removed from memory (if no other references exist).

Why There's No Need for del self?
    The __del__ method is part of the cleanup process and is automatically triggered by Python when the object is no longer needed. You don't need to manually delete it using del self—Python handles this for you.

What is the Garbage Collector?
    The garbage collector in Python is a background system responsible for managing memory by:

        - Automatically deallocating objects that are no longer used (when their reference count drops to zero).
        - Detecting and handling circular references that cannot be cleaned up by simple reference counting.
        - Using the gc module to allow developers to:
            Trigger garbage collection manually (gc.collect()).
            Inspect objects tracked by the garbage collector.
            Adjust garbage collection thresholds.

Circular References:
    If two or more objects reference each other, they may form a circular reference.
    Even if there are no external references to these objects, their reference count won't drop to zero.
    Python's garbage collector can handle this situation by periodically checking for cycles and cleaning them up.    

Additional Points:
    The Role of Circular References:
        Python's garbage collector uses reference counting to determine when objects can be deleted.
        Circular references (e.g., two objects referencing each other) can prevent reference counts from reaching zero. In such cases, Python's garbage collector uses an additional mechanism to detect and break cycles, allowing the objects to be deleted.
    Explicit Deletion vs Garbage Collection:
        Even after using del obj, the object might not be immediately destroyed if:
        There are other references.
        The garbage collector hasn't yet run to clean up memory.
    __del__ Pitfalls:
        Be cautious with __del__ because if exceptions occur during its execution, they are ignored.
        Using __del__ inappropriately (e.g., relying on it for critical cleanup) can lead to resource leaks.

What Happens If __del__ is Not Defined?
    If the __del__ method is not defined in your class, Python will:
        Automatically reclaim the memory for the object when its reference count drops to zero.
        Skip the step of calling a __del__ method because there’s none to call.
What Happens If __del__ is Defined?
    If you define a __del__ method in your class, Python:
        Calls your __del__ method before the object is deallocated.
        Performs any custom cleanup actions you’ve defined in the method.
        Reclaims the memory for the object afterward.

Recap:
    del obj and References:
        If obj is the only reference to an object, then del obj will:
        Remove the reference.
        Trigger the garbage collector to delete the object from memory.
        If there are other references (e.g., ref = obj), then del obj will only remove the obj reference. The object in memory remains because the reference ref still exists. The garbage collector won't delete the object until all references are removed.
    Garbage Collector's Role:
        Python's garbage collector automatically frees memory by deallocating objects no longer in use (i.e., objects with zero references).
    __del__ Implementation:
        If you don’t define __del__, the garbage collector silently deletes the object without performing any custom actions.
        If you do define __del__, it is called before the object is deleted from memory. This allows you to add custom cleanup actions (e.g., printing a message, closing files, etc.).
    Behavior of __del__:
        When __del__ is defined, it executes before the object is deallocated but does not itself delete the object. The actual memory cleanup is still handled by the garbage collector.
"""
# Example:
import gc

class Example:
    def __del__(self):
        print("Object is being deleted.")

# Create two objects referencing each other (circular reference)
obj1 = Example()
obj2 = Example()
obj1.partner = obj2
obj2.partner = obj1

# Delete both references
del obj1
del obj2

# Force garbage collection
gc.collect()  # Output: Object is being deleted. (twice)

# Why use gc.collect()?
#     In this case, a circular reference prevents automatic cleanup. The garbage collector detects it during its periodic check "فحص دوري" or when you explicitly "بصراحة" call gc.collect().



# example
# without __del__
class Example:
    pass

obj = Example()
del obj  # The object is deleted, but no message or custom actions occur.


# with __del__
class Example:
    def __del__(self):
        print("Object is being deleted.")

obj = Example()
del obj  # Output: "Object is being deleted."



# example
class Example:
    def __del__(self):
        print(f"Deleting object: {id(self)}")

# Create an object
obj = Example()
ref = obj  # Another reference to the same object

# Delete obj (but the object isn't deleted yet because of ref)
del obj
print("After del obj")

# Delete ref (now the object is eligible for garbage collection)
del ref
print("After del ref")

# Force garbage collection to see the __del__ message
gc.collect()
