from abc import ABC, abstractmethod


"""
Polymorphism in OOP
    Polymorphism is a fundamental concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying forms (data types). The term "polymorphism" comes from the Greek words poly (many) and morph (forms), meaning "many forms."


Simplified Definition of Polymorphism
    Polymorphism means "one thing, many forms." In programming, it allows objects from different classes to use the same method name, and the correct method is automatically chosen based on the object's type.

    
Analogy:
    Think of a remote control. The same "Play" button can play:
    A movie on a TV.
    A song on a music player.
    A video on a projector.


Polymorphism can occur in different forms:
    Method Overriding (Runtime Polymorphism)
    Method Overloading (Not directly supported in Python but can be mimicked)
    Operator Overloading


Advantages of Polymorphism
    Flexibility: You can write more flexible and reusable code.
    Extensibility: Adding new behaviors becomes easier.
    Code Simplification: It allows one interface to be used for different types.
"""

#----------------------------------------------------------------

"""
Method Overriding (Runtime Polymorphism)
    In method overriding, a subclass provides its own implementation of a method that is already defined in the parent class. This is the most common form of polymorphism.
"""
# example
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

# Polymorphism in action
animals = [Animal(), Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# The speak() method is overridden in Dog and Cat classes.
# The speak() method is called on each object, but the implementation depends on the actual type of the object.


#----------------------------------------------------------------

"""
Operator Overloading
    In Python, polymorphism is extended to operators. This means you can define the behavior of operators (+, -, *, etc.) for your custom classes by implementing special methods called dunder methods (double underscore methods).

operator overloading works by overriding special methods (also called dunder methods). These names are reserved for specific operators. You cannot use custom names for these methods.

If you try to use a different name like add() instead of __add__, it won’t work with the + operator.
"""
# example
class Math:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f"({self.num1}, {self.num2})"

    def check_zero_division(self, other):
        """ Helper method to check if division by zero is attempted. """
        if other.num1 == 0 or other.num2 == 0:
            return True
        return False
    
    def __add__(self, other):
        return (self.num1 + other.num1) + (self.num2 + other.num2)
    
    def __sub__(self, other):
        return (self.num1 - other.num1) - (self.num2 - other.num2)
    
    def __mul__(self, other):
        return (self.num1 * other.num1) * (self.num2 * other.num2)
    
    def __truediv__(self, other):
        if self.check_zero_division(other):
            return "Error: Division by zero is not allowed."
        return (self.num1 / other.num1) / (self.num2 / other.num2)
    
    def __floordiv__(self, other):
        if self.check_zero_division(other):
            return "Error: Division by zero is not allowed."
        return (self.num1 // other.num1) // (self.num2 // other.num2)
    
    def __mod__(self, other):
        if self.check_zero_division(other):
            return "Error: Modulus by zero is not allowed."
        return (self.num1 % other.num1) % (self.num2 % other.num2)
    

obj1 = Math(8, 6)
obj2 = Math(6, 4)

print(obj1)  # (8, 6)
print(obj2)  # (6, 4)
print("Addition:", obj1 + obj2)           # (8+6) + (6+4) = 24
print("Subtraction:", obj1 - obj2)        # (8-6) - (6-4) = 2
print("Multiplication:", obj1 * obj2)     # (8*6) * (6*4) = 1152
print("Division (float):", obj1 / obj2)   # (8/6) / (6/4) = 0.888...
print("Floor Division:", obj1 // obj2)    # (8//6) // (6//4) = 0
print("Modulus:", obj1 % obj2)            # (8%6) % (6%4) = 2



# example
class ComplexNumbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}j"
    
    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return complex(self.real - other.real, self.imag - other.imag)
    
c1 = ComplexNumbers(1, 2)
c2 = ComplexNumbers(3, 4)
print(c1)   # Output: 1 + 2J
print(c2)   # Output: 3 + 4J
print(c1 + c2)  # Output: 4 + 6J
print(c1 - c2)  # Output: -2 - 2J
print(c2 - c1)  # Output: 2 + 2J
print(ComplexNumbers.__add__(c1, c2))  # Output: 4 + 6J
print(c1.__sub__(c2)) # Output: -2-2j


# example
class Order:
    def __init__(self, cart, first_name, second_name):
        self.cart = cart
        self.first_name = first_name
        self.second_name = second_name

    def __len__(self):
        return len(self.cart)
    
    def __add__(self, first, second):
        return first + " " + second
    
    def __str__(self):
        return f"Order: {self.cart} placed by {self.__add__(self.first_name, self.second_name)}"
    
    def __eq__(self, other):
        return self.__len__() == other.__len__()
    
    def __bool__(self):
        return bool(self.cart)
    
order1 = Order(["apples", "banana"], "Islam", "Ahmed")
order2 = Order(["apples", "banana"], "Mohamed", "Ahmed")
order3 = Order([], "Ibrahem", "Ahmed")
print(order1.__add__(order1.first_name, order2.first_name))  # Islam Mohamed
order1.cart.append("Orange")  
print(len(order1.cart))  # 3
print(order1)  # Order: ['apples', 'banana', 'Orange'] placed by Islam Ahmed
print(order1 == order2)  # False
if not order3:
    print("Order3 is empty.")

#----------------------------------------------------------------

"""
Polymorphism with Functions and Objects
    Python functions can accept arguments of any type and behave differently based on the input, demonstrating polymorphism.
"""
# example
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def describe(self):
        return f"This shape is {self.color}."
    

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def describe(self):
        # return the full description, including the superclass description
        base_description = super().describe()
        return f"{base_description}. It is a rectangle with a width of {self.width} and a height of {self.height}."
    

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    

def calculate_area(shape):
    return shape.area()

rectangle = Rectangle("red", 2, 3)
circle = Circle("blue", 4)

shapes = [rectangle, circle]
for shape in shapes:
    print(shape.describe())
    print(calculate_area(shape))


#----------------------------------------------------------------

"""
Polymorphism in Class Hierarchies
    In a class hierarchy, polymorphism allows a single method call to work with different subclasses.
or
Different classes in the same hierarchy can implement the same method differently.
"""

class Vehicle:
    def fuel_type(self):
        return "Some fuel"

class Car(Vehicle):
    def fuel_type(self):
        return "Petrol"

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"

# Polymorphism in action
vehicles = [Vehicle(), Car(), ElectricCar()]
for vehicle in vehicles:
    print(vehicle.fuel_type())


#----------------------------------------------------------------

"""
What is Method Overloading?
    Method Overloading means having multiple methods with the same name but different numbers or types of parameters in the same class.

Python's Behavior:
    Python does not directly support method overloading. If you define two methods with the same name, the last one will overwrite the first. However, you can mimic "تقلد" overloading using:

    Default arguments.
    Variable-length arguments (*args, **kwargs).
"""

class Calculator:
    def add(self, a, b, c=0):  # Third parameter is optional
        return a + b + c

calc = Calculator()
print(calc.add(2, 3))       # Output: 5
print(calc.add(2, 3, 4))    # Output: 9


#----------------------------------------------------------------

"""
Is Implementing Abstract Methods Polymorphism?
    Yes, implementing abstract methods in subclasses is a form of polymorphism. Here's why:

    Abstract Method Implementation: When a subclass provides its own version of an abstract method, the method is used polymorphically based on the object's type.
"""

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return "Area of Circle"

class Square(Shape):
    def area(self):
        return "Area of Square"

# Polymorphism in action
shapes = [Circle(), Square()]
for shape in shapes:
    print(shape.area())

"""
Here, the abstract method area() is implemented differently in Circle and Square. When called, the correct version is chosen automatically.

Overriding Concrete Methods: If a subclass overrides a concrete method from an abstract class, it is also considered polymorphism. The same method name (method()) behaves differently based on the object's type.
"""
