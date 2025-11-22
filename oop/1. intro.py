### Classes, objects, attributes , methods


"""
Classes
A class is a blueprint for creating objects (instances). It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.

Defining a Class
You define a class using the class keyword, followed by the class name. By convention, class names are written in CamelCase.
"""

class Dog:
    # Attributes (Properties)
    species = "Canis familiaris"  # This is a class attribute, shared by all instances

    def __init__(self, name, age):
        # Instance attributes (specific to each object)
        self.name = name
        self.age = age

    # Method (Behavior)
    def bark(self):
        print(f"{self.name} says Woof!")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")


#----------------------------------------------------------------

"""
Objects
An object is an instance of a class. Once a class is defined, you can create instances (objects) of that class. Each object has its own set of attributes and can call the class methods.

Creating Objects
You create an object by calling the class name like a function, passing any required arguments (e.g., the name and age of the dog).
"""

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Bella", 5)

# Accessing attributes and calling methods
print(dog1.name)  # Output: Buddy
dog1.bark()  # Output: Buddy says Woof!
dog1.describe()  # Output: Buddy is 3 years old.

print(dog2.name)  # Output: Bella
dog2.bark()  # Output: Bella says Woof!
dog2.describe()  # Output: Bella is 5 years old.

#----------------------------------------------------------------

"""
The __init__ Method
The __init__ method is the constructor of a class. It is automatically called when an object is created from the class. It’s used to initialize the object's attributes.

in the example above

def __init__(self, name, age):
    self.name = name
    self.age = age

self refers to the instance of the object being created (i.e., the new object).
name and age are the parameters that will be used to set the name and age attributes of the object.
"""

#----------------------------------------------------------------

"""
Instance vs Class Attributes

Instance attributes are specific to each object. In the example, self.name and self.age are instance attributes.
Class attributes are shared by all instances of the class. In the example, species is a class attribute.
"""

# You can access class attributes through the class name or via an object:
print(Dog.species)  # Output: Canis familiaris
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris

"""
Modifying Class Attributes
You can change class attributes for all objects or specific ones.
"""
Dog.species = "Canis lupus familiaris"     # changing it for all instances of the class
# dog1.species = "Canis lupus familiaris"  # changing it for dog1 instance only
print(dog1.species)  # Output: Canis lupus familiaris
print(dog2.species)  # Output: Canis lupus familiaris

print(dog1.name)
del dog1.name  # delete name attribute for dog1 instance
# print(dog1.name)  # AttributeError: 'Dog' object has no attribute 'name'
print(dog2.name)  # Output: Bella


#----------------------------------------------------------------

"""
Instance Methods
Instance methods are functions defined inside a class that operate on an instance of the class. They can access and modify the object's attributes.
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increase_age(self):
        self.age += 1
        print(f"{self.name}'s age is now {self.age}.")
        
# Usage
dog = Dog("Buddy", 3)
dog.increase_age()  # Buddy's age is now 4.

#----------------------------------------------------------------

"""
Comparing Objects
You can compare objects by comparing their attributes. This can be useful to check if two objects are "equal" in some sense.
"""
class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_same_age(self, otherChild):
        return self.age == otherChild.age
    
    # def __str__(self):
    #     #  return f"<__main__.Child object at {hex(id(self))}>"  # return the memory address of the object
    #     return f"Child with name {self.name} is {self.age} years old"
    
    def __repr__(self):
        # return f"<__main__.Child object at {hex(id(self))}>"  # return the memory address of the object
        return f"Child with name {self.name} is {self.age} years old"
    

myChild = Child("Ahmd", 3)
anotherChild = Child("Nour", 2)
print(myChild.is_same_age(anotherChild))

# to print the class instance, the default output will be "<__main__.Class object at memory address>"
# and we can override this behavior by defining __str__ method or __repr__ method and returning another string
print(myChild)  # Output: Child with name Ahmd is 3 years old

#----------------------------------------------------------------

"""
In Python, both @classmethod and @staticmethod are decorators used to define special types of methods in a class.
"""

"""
@classmethod
A class method is bound to the class and not the instance.
It takes cls (the class itself) as its first parameter instead of self (the instance).
It can modify or access the class state (class variables).
It is typically used for creating alternative constructors or working with class-level data.

When Should You Use @classmethod?
Use it when you need to perform operations that affect the class as a whole (e.g., modifying a class attribute).
If you don't intend to affect the class state, but need a method that doesn’t interact with instance attributes, consider using @staticmethod instead.

Class methods can only access class attributes, not instance attributes, because they operate at the class level (cls).
To work with instance attributes in a class method, you need to explicitly pass an instance as an argument, the last example showing that.

Syntax:
class MyClass:
    @classmethod
    def my_class_method(cls, *args):
        # cls refers to the class
        pass
"""

class Dog:
    species = "Canis familiaris"  # Class attribute shared by all instances
    
    def __init__(self, name):
        self.name = name  # Instance attribute unique to each object

    @classmethod
    def change_species(cls, new_species):
        # cls refers to the Dog class, not the instance
        cls.species = new_species

# Access class attribute through the class
print(Dog.species)  # Output: Canis familiaris

# Call @classmethod through the class
Dog.change_species("bla bla bla")
print(Dog.species)  # Output: bla bla bla

# Create an instance
dog1 = Dog("bla")

# Call @classmethod through the instance
dog1.change_species("bla bla 2")  # cls still refers to Dog class
print(dog1.species)  # Output: bla bla 2
"""
Why Does @classmethod Work with an Instance?
When you call a @classmethod using an instance (e.g., dog1.change_species("bla bla 2")), Python automatically passes the class (Dog) as the first argument to the method, not the instance (dog1).

So, the cls parameter inside the change_species method still refers to the Dog class, even when the method is called on an instance.
"""


# classmethods can be used as an alternative constructor

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

person = Person.from_string("Islam,29")
print(person.name)  # Islam
print(person.age)  # 29



"""
@staticmethod
A static method is bound to the class, but it doesn’t access or modify the class or instance state.
It takes neither cls nor self as its first parameter.
It behaves like a regular function defined inside a class but is included in the class's namespace.
It is typically used for utility functions related to the class but not dependent on class or instance state.
Static methods are ideal for utility functions or logic that doesn't depend on the class or instance but is related to the class's domain.
They provide logical grouping, keeping the function within the class for better organization.

Syntax:
class MyClass:
    @staticmethod
    def my_static_method(*args):
        # No access to self or cls
        pass
"""

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b
    
# access using class directly
print(MathUtils.add(1, 2))  # 3
print(MathUtils.subtract(5, 3))  # 2

# access using an instance of the class
math = MathUtils()
print(math.add(1, 2))  # 3
print(math.subtract(5, 3))  # 2


# Static methods can be used as Helper or utility functions
class Validator:
    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 120

# Usage
print(Validator.is_valid_age(25))  # Output: True
print(Validator.is_valid_age(150))  # Output: False


#----------------------------------------------------------------

# Here's a summary to clarify the distinction between class methods, static methods, instance methods, class attributes, and instance attributes:


"""
Class Methods
    Definition: 
        Defined with the @classmethod decorator. The first parameter is cls, which refers to the class itself.
    Access:
        Can be called on the class directly (e.g., ClassName.method()).
        Can also be called on an instance (e.g., instance.method()), but cls will still refer to the class.
    Scope:
        Works with class attributes and can modify the class state.
"""
#Example:
class Example:
    class_var = "class attribute"

    @classmethod
    def change_class_var(cls, value):
        cls.class_var = value

# Call via class
Example.change_class_var("new value")
print(Example.class_var)  # Output: new value

# Call via instance
instance = Example()
instance.change_class_var("another value")
print(Example.class_var)  # Output: another value


"""
Static Methods
    Definition: 
        Defined using the @staticmethod decorator. They don’t take self or cls as parameters and behave like regular functions but are grouped logically within the class.
    Access:
        Can be called via the class (e.g., ClassName.method()).
        Can also be called via an instance (e.g., instance.method()).
    Scope: 
        Independent of class and instance. They cannot modify or access class or instance attributes.
"""
#Example:
class Utility:
    @staticmethod
    def add(a, b):
        return a + b

# Call via class
print(Utility.add(3, 5))  # Output: 8

# Call via instance
utility_instance = Utility()
print(utility_instance.add(7, 2))  # Output: 9


"""
Instance Methods
    Definition:
        Regular methods defined in a class, taking self as the first parameter. self refers to the instance calling the method.
    Access:
        Must be called on an instance (e.g., instance.method()). They cannot be called directly on the class because they operate on instance-specific data.
    Scope: 
        Works with instance attributes and can modify the state of that particular instance.
"""
#Example:
class Example:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

instance = Example("John")
print(instance.name)  # Output: John
instance.change_name("Jane")
print(instance.name)  # Output: Jane


"""
Class Attributes
    Definition: 
        Variables defined at the class level, shared among all instances of the class.
    Access:
        Can be accessed or modified via the class (e.g., ClassName.attribute).
        Can also be accessed via an instance (e.g., instance.attribute), but they belong to the class.
    Scope:
        Shared by all instances of the class.
"""
#Example:
class Example:
    shared_var = "shared"

instance1 = Example()
instance2 = Example()

print(instance1.shared_var)  # Output: shared
Example.shared_var = "modified"
print(instance2.shared_var)  # Output: modified


"""
Instance Attributes
    Definition: 
        Variables defined for each instance, typically inside the __init__ method.
    Access: 
        Can only be accessed or modified through an instance.
    Scope: 
        Unique to each instance.
"""
#Example:
class Example:
    def __init__(self, name):
        self.name = name  # Instance attribute

instance1 = Example("Alice")
instance2 = Example("Bob")

print(instance1.name)  # Output: Alice
print(instance2.name)  # Output: Bob



"""
Summary:

Class methods, static methods, and class attributes: Accessible via both the class and its instances but operate at the class level.
Instance methods and instance attributes: Tied to individual objects and cannot be used directly with the class.
"""

# Full Example:
class FullExample:
    # Class attribute (shared across all instances and the class itself)
    classAttr = "This is a class attribute"

    def __init__(self, name):
        # Instance attribute (unique to each instance)
        self.name = name

    # Class method
    @classmethod
    def class_method(cls, instance, text):
        # Accessing instance attribute by explicitly passing the instance
        # cls refers to the class itself, not an instance
        return f"Access to instance attribute (name) via passed instance: {instance.name}, and text is: {text}"

    # Static method
    @staticmethod
    def static_method(text):
        # Independent of both class and instance attributes
        # Acts like a regular function, but grouped logically within the class
        return text

    # Instance method
    def instance_method(self):
        # Accessing instance-specific data using 'self'
        print(f"Hello, my name is {self.name}")


# Access class attribute directly via the class
print(FullExample.classAttr)  # Output: This is a class attribute

# Create an instance of the class
example = FullExample("example")

# Call an instance method (requires an instance)
example.instance_method()  # Output: Hello, my name is example

# Modify class attribute directly via the class
FullExample.classAttr = "This is a class attribute updated"
print(FullExample.classAttr)  # Output: This is a class attribute updated

# Assigning a new attribute to the instance with the same name as the class attribute
example.classAttr = "This is a class attribute again"
# Instance-specific attribute hides the class attribute when accessed via the instance
print(example.classAttr)  # Output: This is a class attribute again

# Accessing the class method
# Passing the instance explicitly to access its instance attribute
print(example.class_method(example, "bla bla"))
# Output: Access to instance attribute (name) via passed instance: example, and text is: bla bla

# Call the class method directly from the class
# Pass a new instance as the argument to access its attributes
print(FullExample.class_method(FullExample("example 2"), "bla bla bla"))
# Output: Access to instance attribute (name) via passed instance: example 2, and text is: bla bla bla

# Call static method from the class
print(FullExample.static_method("bla bla bla"))  # Output: bla bla bla

# Call static method from the instance
print(example.static_method("bla bla bla bla"))  # Output: bla bla bla bla
