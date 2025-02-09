"""
Abstraction is a fundamental concept in OOP that focuses on hiding the internal implementation details of a system and exposing only the essential features to the user. It provides a way to separate the what from the how, allowing the user to interact with an object or method without worrying about its inner workings.

How is Abstraction Achieved?
    Abstract Classes:
        An abstract class is a class that cannot be instantiated directly.
        It serves as a blueprint for other classes.
        Contains abstract methods (methods without implementation) that must be overridden in subclasses.
    Interfaces:
        In some languages, interfaces define the required methods that implementing classes must provide.
        In Python, the closest equivalent is using abstract base classes (ABCs).


Python's Abstract Base Classes (ABCs)
    Python uses the abc module to create abstract classes. An abstract class can have:
        Abstract methods: Defined with no implementation.
        Concrete methods: Normal methods with implementation.


Advantages of Abstraction
    Simplifies Code: The user interacts only with the exposed functionality, not the implementation.
    Improves Maintainability: Changes in the internal logic don’t affect the external interface.
    Promotes Reusability: Abstract classes provide a common template for different subclasses.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def common_behavior(self):
        return "All animals need food and water."


# Subclass providing the implementation
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())  # Calls the concrete implementation in each subclass


#----------------------------------------------------------------

"""
different between Abstraction and Encapsulation


## Abstraction

definition: Hiding the implementation details while exposing only the functionality to the user.

focus: What functionality is provided (hiding complexity behind an interface).

implementation: Achieved through abstract classes, interfaces, or methods.

purpose: Simplify interactions by exposing only what is necessary.

scope: Operates at the level of class or system design.

example: Using abstract methods in an abstract base class that are implemented by subclasses.


## Encapsulation

definition: Hiding the internal state and requiring all interaction to happen through well-defined methods.

focus: How data is accessed and modified (restricting direct access).

implementation: Achieved through access modifiers (e.g., public, protected, private).

purpose: Protect sensitive data and ensure integrity.

scope: Operates at the level of attributes and methods inside a class.

example: Using private attributes (__attr) and methods, accessed via getters and setters.
"""

# Encapsulation example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

# User doesn't directly access __balance but interacts via methods.
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# Here, the balance is encapsulated to ensure that it cannot be directly modified, protecting the integrity of the data.


# Abstraction example
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

# The user only knows the Payment interface, not the implementation details.
payment_methods = [CreditCardPayment(), PayPalPayment()]
for method in payment_methods:
    print(method.process_payment(100))
# Here, the user interacts with the process_payment method without worrying about how the payment is actually processed for each payment method.


"""
Key Difference in "Hiding"
    Encapsulation hides data within a class and restricts access to it using access modifiers.
    Example: Hiding __balance and providing controlled access via methods.

    Abstraction hides the implementation details and provides a clean interface.
    Example: Hiding how process_payment is implemented for each payment method and exposing only the method signature.
"""

#----------------------------------------------------------------

"""
What Are Interfaces in OOP?
    In many object-oriented languages, an interface is a type that defines a contract, which specifies a set of methods that a class must implement. The key point about interfaces is that they define what methods should be present, but not how those methods are implemented.
    For example:

        In Java or C#, an interface defines methods without implementation, and any class that implements this interface must provide its own implementation for these methods.
        In Python, we achieve a similar effect using Abstract Base Classes (ABCs).

    While Python does not have a built-in interface mechanism, we can use abstract classes to accomplish the same thing.


What Does ABC Mean in Python?
    ABC stands for Abstract Base Class, which is a class in Python that cannot be instantiated directly and is meant to be subclassed. It allows you to define abstract methods that must be implemented in any subclass.

    An abstract class can contain both abstract methods (methods without implementation) and regular methods (methods with implementation).
    In Python, we use the abc module to create abstract classes and define abstract methods.
"""

class Shape(ABC):
    @abstractmethod
    def area(self):   # This method must be implemented by subclasses
        pass

    def description(self):
        print("This is a shape.")  # Regular method with implementation
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2    # # Concrete implementation
    
class Rectangle(Shape):  # Another subclass implementing abstract methods
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Concrete implementation
    
    def description(self):
        super().description()
        return "This is a rectangle."  # Concrete implementation
# Usage
circle = Circle(5)
print(circle.area())  # Output: 78.5
circle.description()  # Output: This is a shape

rectangle = Rectangle(4, 6)
print(rectangle.area())  # Output: 24
print(rectangle.description())  # Output: This is a shape. \n This is a rectangle

"""
Can an Abstract Class Have Regular Methods?
    Yes, abstract classes can have regular methods that are implemented. Subclasses can inherit these regular methods without overriding them, or they can override them if needed.

    In the previous example, the description() method is a regular method in the abstract Shape class. The Circle class doesn't need to define description() because it inherits it from Shape, but the rectangle class inherites and overrides it
"""

#----------------------------------------------------------------

"""
More about Encapsulation vs Abstraction

    Abstraction vs Encapsulation: 
        Abstraction and encapsulation are both concepts that hide certain details, but they differ in their goals and the level at which they operate:

        Abstraction is about hiding the implementation details of a system, focusing on what an object can do rather than how it does it. The goal is to provide a simplified interface for interaction, leaving out unnecessary complexity.
        Example: In an abstract class, you define methods without specifying their implementation, allowing subclasses to provide specific implementations. This hides the "how" of the functionality from the user.

        Encapsulation is about hiding the internal state of an object and controlling how that state is accessed and modified. It focuses on the "how" data is stored and accessed. Encapsulation protects data by making it private and only allowing modification through public methods (getters and setters).
        Example: A class with private attributes that are accessed or modified through getter and setter methods, ensuring that the internal state remains consistent and protected.

        
    Key Differences:

        Abstraction focuses on hiding the complexity of the system and exposing only what is necessary, typically through abstract classes or interfaces, and is concerned with providing a clear and simple interface.

        Encapsulation focuses on hiding the internal state of an object and controlling access to that state, often using access modifiers (private, protected) and methods to access or modify the data.


    In summary:

        Abstraction hides the complexity of the system and provides an interface that allows users to interact with objects without needing to understand how the internal workings are implemented.
        
        Encapsulation hides the internal data and ensures that it can only be accessed or modified through a controlled interface, protecting the integrity of the data.
"""