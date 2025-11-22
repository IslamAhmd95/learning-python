"""
Inheritance is one of the core principles of Object-Oriented Programming (OOP). It allows you to define a new class (called a subclass or child class) based on an existing class (called a superclass or parent class). The subclass inherits the attributes and methods of the parent class and can also define its own unique behavior. This allows for code reuse, modularity, and a hierarchical relationship between classes.

Inheritance is fundamental for modeling real-world relationships. For example, in a class hierarchy, a Dog can inherit from an Animal, meaning a Dog is an Animal, and it can share behaviors (methods) like eat() or sleep() but also define behaviors unique to dogs, such as bark().


Key Concepts in Inheritance
    Parent Class: The class that is being inherited from (also called the superclass).
    Child Class: The class that inherits from the parent class (also called the subclass).
    Overriding: The ability of the child class to define its own version of a method that is already defined in the parent class.
    Extending: The ability of the child class to add new methods or properties to the inherited functionality.
"""

# example
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I'm {self.name}!")

    def get_age(self):
        print("This is for age")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        super().get_age()  # Call the parent method to print the default age message
        print(f"I am {self.age} years old.")

child = Child("John", 20)
child.greet()  # Output: Hello, I'm John!
child.get_age()  # Output: This is for age \n I am 20 years old.



# example
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle brand: {self.brand}, model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, wheels=4):
        super().__init__(brand, model)  # Inherit the parent class's constructor
        self.wheels = wheels

    def display_info(self):
        super().display_info()  # Call the parent class's method
        print(f"Number of wheels: {self.wheels}")

# Usage
car = Car("Toyota", "Corolla", 8)
car.display_info() # Output: Vehicle brand: Toyota, model: Corolla \n Number of wheels: 8
# Method Overriding: The Car class overrides the display_info() method of Vehicle to extend its functionality (e.g., showing the number of wheels).



# example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I'm {self.name} and my age is {self.age}!")


class Employee:
    def __init__(self, job_title):
        self.job_title = job_title

    def job(self):
        print(f"I'm an employee and my job title is {self.job_title}!")

class Manager(Person, Employee):
    def __init__(self, name, age, job_title):
        Person.__init__(self, name, age)
        Employee.__init__(self, job_title)


# Usage
manager = Manager("Alice", 35, "Project Manager")
manager.greet()  # Output: Hello, I'm Alice and my age is 35.
manager.job()    # Output: I'm an employee and my job title is Project Manager.




"""
Example 4: Method Resolution Order (MRO) in Multiple Inheritance
    In case of multiple inheritance, Python uses the Method Resolution Order (MRO) to decide which method to call when a method is inherited from multiple classes.
"""
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        print("Hello from B")

class C(A):
    def hello(self):
        print("Hello from C")

class D(B, C):
    pass

# Usage
d = D()
d.hello()  # Output: Hello from B
# Class D inherits from both B and C, and both B and C inherit from A.
# When we call hello() on an object of D, Python follows the MRO and calls the hello() method from B because it comes first in the inheritance list.


"""
Inheritance Terminology  "مصطلحات"

    Parent class (also called superclass or base class) is the class whose properties and methods are inherited by another class.

    Child class (also called subclass) is the class that inherits from the parent class and can extend or override its behavior.

    Overriding means defining a method in the child class that has the same name as a method in the parent class but provides a different implementation.

    Extending means adding new methods and properties in the child class that are not present in the parent class.

    
Advantages of Inheritance

    Code Reusability: The child class can reuse methods and attributes of the parent class, which reduces code duplication.
    Organization: Inheritance provides a clear structure, making it easier to represent real-world relationships between objects.
    Extensibility: New functionality can be added in subclasses without modifying the parent class.
    Maintainability: Changes in the parent class can automatically propagate to child classes, making code easier to maintain.


Summary of Inheritance

    Inheritance allows you to create a new class that builds upon an existing class, reusing its attributes and methods.
    You can extend functionality in the child class and override inherited methods to customize behavior.
    Python supports both single inheritance and multiple inheritance.
    In case of multiple inheritance, Python uses Method Resolution Order (MRO) to determine the method to call.
"""

#----------------------------------------------------------------

"""
Multiple Inheritance in Python
Multiple inheritance allows a class to inherit from more than one parent class.

Syntax:
    class Parent1:
        pass

    class Parent2:
        pass

    class Child(Parent1, Parent2):
        pass

"""

# Problem in Multiple Inheritance
# If both parent classes have a method with the same name, which one does Python use?
class A:
    def show(self):
        print("A's show")

class B:
    def show(self):
        print("B's show")

class C(A, B):
    pass

obj = C()
obj.show()  # A's show
# Python looks for the show() method in the order of inheritance: C(A, B) → Python checks A first, then B.


# Method Resolution Order (MRO)
# MRO defines the order in which Python looks for a method in the inheritance hierarchy.
print(C.mro())  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# OR
# help(C)  



"""
C3 Linearization Algorithm
    Python uses the C3 Linearization algorithm to handle MRO.
    It follows these rules:
        Child → Parent (Left to Right)
        No duplication of classes
        Preserve local order of classes
"""

# Complex Example: Diamond Problem
class A:
    def show(self):
        print("A's show")

class B(A):
    def show(self):
        print("B's show")

class C(A):
    def show(self):
        print("C's show")

class D(B, C):
    pass

obj = D()
obj.show()  # B's show
print(D.mro())  # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
"""
Order Explanation:
    Python checks D → no show()
    Checks B → found show() → Stops here
    C and A are ignored
"""


# Using super() in Multiple Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(A):
    def show(self):
        print("C")
        super().show()

class D(B, C):
    def show(self):
        print("D")
        super().show()

obj = D()
print(D.mro())
obj.show()
"""
Output:
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
D  
B  
C  
A

Execution Breakdown
    D.show() is called → prints "D".
    super().show() in D → goes to B (next in MRO).
    B.show() → prints "B".
    super().show() in B → goes to C, not A!
    Because MRO says C comes after B.
    C.show() → prints "C".
    super().show() in C → goes to A.
    A.show() → prints "A".
    Done!


Why Does super().show() in B Call C.show() Instead of A.show()?
    In multiple inheritance, super() does not mean "call the method in the immediate parent."
    Instead, it follows the MRO (Method Resolution Order).

Why Not Directly to A from B?
    super() follows the MRO, not the parent class in the code.
    Since C is next after B in the MRO, Python calls C.show().

Key Rule:
    super() in Python always respects MRO, not direct inheritance.
"""


"""
MRO in Single Inheritance:
    Child → Parent → object
In a Single Class:
    Class → object
Using super() in a base class can cause errors if the next class doesn’t have the method.
"""
# Case 1: Single Inheritance (One Parent, One Child)
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")
        super().show()

obj = B()
print(B.mro())  # [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
obj.show() # B A



# Case 2: Single Class Without Inheritance
class A:
    def show(self):
        print("A")
        super().show()  # Using super here!

obj = A()
print(obj.mro())  # [<class '__main__.A'>, <class 'object'>]
# obj.show()  # AttributeError: 'super' object has no attribute 'show'
"""
Why the Error?
    super().show() tries to call show() in the next class in the MRO, which is object.
    But object doesn't have a show() method.

How to Avoid the Error?
    Option 1: Add a default show() method in A without calling super().
    Option 2: Use a safe check:
"""
class A:
    def show(self):
        print("A")
        if hasattr(super(), 'show'):
            super().show()

obj = A()
obj.show()


#----------------------------------------------------------------

"""
Object is the base class for all new-style classes. This means that every class in Python implicitly inherits from object, even if you don’t explicitly specify it.

Why Does Python Use object as the Base Class?
    It provides a common foundation for all classes.
    Supplies default behaviors (methods) that every object in Python can use, like:
        __init__() – Constructor
        __str__() – String representation
        __repr__() – Official string representation
        __eq__() – Equality comparison
        __hash__() – Hash value
        __class__ – Reference to the class of the object
"""
# Implicit Inheritance:
class A:
    pass

print(A.mro())  # [<class '__main__.A'>, <class 'object'>]
# Even though we didn’t write class A(object):, Python automatically makes A inherit from object.


# Explicit Inheritance:
class B(object):
    pass

print(B.mro())  # [<class '__main__.B'>, <class 'object'>]



# How object Affects Custom Classes
class A:
    pass

a = A()
print(a)  # <__main__.A object at 0x...>
# This default behavior comes from object's __str__() method.


"""
Old-Style vs. New-Style Classes (Python 2 vs. Python 3)
    In Python 2, if you didn't inherit from object, you'd create an "old-style" class.
    In Python 3, all classes are new-style and automatically inherit from object.

In Python 2, classes were divided into two types:
    Old-Style Classes
    New-Style Classes
This distinction was removed in Python 3, where all classes are new-style by default.

1. Old-Style Classes
    Created without explicitly inheriting from object.
    Lacked many modern features, such as consistent method resolution.
    Example:
        # Python 2 old-style class
        class OldClass:
            pass


2. New-Style Classes
    Created by explicitly inheriting from object.
    Introduced in Python 2.2 to unify types and classes.
    Example:
        # Python 2 new-style class
        class NewClass(object):
            pass
            
# # Example: MRO Difference

# Old-Style Class (DFS Order):
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.show()  # D → B → A → C → A,  Risk: Duplicate lookup of A!


# New-Style Class (C3 Linearization Order):
class A(object):
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.show()  # D → B → C → A → object


In Python 2 old-style classes, the Method Resolution Order (MRO) was determined using Depth-First Search (DFS). This approach follows the inheritance chain deeply before moving sideways.

How DFS Works in Inheritance
    Depth-First Search (DFS) means:
        Python searches the leftmost parent class first.
        It fully explores one branch of inheritance before moving to the next.
        Based on the last example:
            Start at D.
            Move to the first parent → B.
            From B, go to its parent → A.
            After finishing with B, check the second parent → C.
            C also inherits from A, but A is revisited.

Problem with DFS
    Notice that A appears twice in the search order (B → A and C → A).
    This duplication can cause problems like:
        Redundant method calls.
        Inconsistent behavior in complex hierarchies

How Python 3 Fixes This with C3 Linearization
    Python 3 (and Python 2 new-style classes) replaced DFS with C3 Linearization, which:
        Ensures each class appears only once in the MRO.
        Provides a consistent and predictable order.

Summary:
    DFS: Fully explores the first parent before moving to the next.
    Can cause method duplication and unexpected behavior.
    C3 Linearization (used in Python 3) solved these issues by creating a cleaner MRO.
"""






