"""
Getters and Setters in Python
    Getters and setters are public methods used to access (get) and modify (set) private attributes of a class. They allow controlled interaction with private attributes by adding logic or validation during access or updates.

Why Use Getters and Setters?
    Encapsulation:
        Ensures that the internal implementation details of a class are hidden.
        Prevents direct access to private attributes.
    Validation:
        Adds logic to validate or restrict changes to private attributes.
    Flexibility:
        Allows you to modify the internal implementation of a class without affecting external code.
"""

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # getter for name
    def get_name(self):
        return self.__name
    
    # setter for name
    def set_name(self, name):
        if name:
            self.__name = name
        else:
            raise ValueError("Name cannot be empty")
    
    # getter for age
    def get_age(self):
        return self.__age

    # setter for age
    def set_age(self, age):
        if age > 0 and isinstance(age, int):
            self.__age = age
        else:
            raise ValueError("Invalid age")
        
person = Person("Islam", 29)

# Access private attributes using getters
print(person.get_name())  # Islam
print(person.get_age()) # 29

# Update private attributes using setters
person.set_name("John Doe")
print(person.get_name())  # John Doe

# Update private attributes using setters
person.set_age(30)
print(person.get_age())  # 30


"""
Using Python's @property Decorator
    Python provides a more elegant way to define getters and setters using the @property decorator.

Syntax:
    for getter in property
        @property
        def attribute_name(self):
            # getter method
            return self.__attribute_name

    for setter in property
        @attribute_name.setter
        def attribute_name(self, value):
            logic           
"""

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # getter for name
    @property
    def name(self):
        return self.__name

        return self.__name
    
    # setter for name
    @name.setter
    def name(self, name):
        if name:
            self.__name = name
        else:
            raise ValueError("Name cannot be empty")
    
    # getter for age
    @property
    def age(self):
        return self.__age

    # setter for age
    @age.setter
    def age(self, age):
        if age > 0 and isinstance(age, int):
            self.__age = age
        else:
            raise ValueError("Invalid age")
        
person = Person("Islam", 29)

# Access private attributes as if they were public
print(person.name)  # Islam
print(person.age )# 29

# Update private attributes as if they were public
person.name = "John Doe"
print(person.name)  # Islam


# Update private attributes as if they were public
person.age = 30
print(person.age)  # 30


"""
Comparison: Without and With @property
    Without @property:
        person.get_name()      # Access via getter
        person.set_name("Bob") # Update via setter

    With @property:
        person.name           # Access via property
        person.name = "Bob"   # Update via property

The @property approach is cleaner and more Pythonic.
"""

"""
Advantages of Getters and Setters

    Validation:
        Example: Prevent setting negative values for an age attribute.
            @age.setter
            def age(self, age):
                if age > 0:
                    self.__age = age
                else:
                    raise ValueError("Age must be positive")

    Transformation/Logic:
        Example: Automatically convert input to uppercase.
            @name.setter
            def name(self, name):
                self.__name = name.upper()

    Backward Compatibility "explained below":
        If a public attribute needs logic in the future, you can convert it to a getter and setter using @property without breaking existing code.
"""


#------------------------------------------------------------------------------


"""
Backward Compatibility  "التوافق مع الإصدارات السابقة"
    Backward compatibility means changing the internal implementation of a class without requiring any changes in the code that uses it "the code that uses this class outside it". Here's how it relates to @property:
        Initially, you might define a public attribute that can be accessed directly (e.g., person.name).
        Later, if you decide to add logic (e.g., validation, transformation) for that attribute, you can switch to using @property without affecting the existing code that uses person.name.

    This is possible because @property allows you to keep the same syntax (e.g., person.name) while adding custom getter and setter logic.


Summary of Access Levels and Property
    Public Attributes:
        Can be accessed and modified directly (e.g., person.name = "John").
        You can still use @property for public attributes if you need to add logic while getting or setting.

    Protected Attributes (single underscore: _attr):
        Intended for internal use, but technically still accessible from outside the class (e.g., person._name).
        Using @property to expose and manage access is a better practice.

    Private Attributes (double underscore: __attr):
        Cannot be directly accessed from outside the class due to name mangling.
        You must use @property or a public method to access or modify them.
"""

# example for Backward Compatibility
class Person:
    def __init__(self, name):
        # Initially, name is a public attribute
        self.name = name


# Existing Code Using Person
p = Person("Alice")
print(p.name)  # Output: Alice
p.name = "Bob"  # Updates name
print(p.name)  # Output: Bob


# Later, you decide to:
    # Ensure names are always capitalized.
    # Validate that the name is not empty.
# Instead of changing how the attribute is accessed (which would break existing code), you can use the @property decorator:

class Person:
    def __init__(self, name):
        self._name = name  # Change internal storage

    @property
    def name(self):
        # Getter logic
        return self._name.capitalize()

    @name.setter
    def name(self, value):
        # Setter logic
        if value:
            self._name = value
        else:
            raise ValueError("Name cannot be empty")


# Existing Code Using Person (No Changes Needed)
p = Person("Alice")
print(p.name)  # Output: Alice (getter logic applied)
p.name = "bob"  # Setter logic applied
print(p.name)  # Output: Bob (capitalized)

# Without @property, you’d have to change how name is accessed and set (e.g., from obj.name to obj.get_name() and obj.set_name()).
# Any existing code using obj.name would break, forcing you to update it wherever the class is used.



"""
Backward Compatibility can also work with protected and private attributes
    Protected Attributes:
        Already accessible outside the class (e.g., obj._attr).
        @property can be used to add logic while maintaining backward compatibility.
    Private Attributes:
        Only accessible via name mangling (e.g., obj._ClassName__attr).
        @property typically improves usability by creating a clean interface.
"""



# example includes all attributes
class Example:
    def __init__(self, public_attr, protected_attr, private_attr):
        self.public_attr = public_attr               # Public
        self._protected_attr = protected_attr        # Protected
        self.__private_attr = private_attr           # Private

    # Public Attribute with Property
    @property
    def public_attr(self):
        return self._public_attr  # Using an internal storage for logic

    @public_attr.setter
    def public_attr(self, value):
        if value:  # Example logic
            self._public_attr = value.upper()  # Enforce uppercase
        else:
            raise ValueError("Value cannot be empty")

    # Getter and Setter for Protected Attribute
    @property
    def protected_attr(self):
        return self._protected_attr

    @protected_attr.setter
    def protected_attr(self, value):
        self._protected_attr = value

    # Getter and Setter for Private Attribute
    @property
    def private_attr(self):
        return self.__private_attr

    @private_attr.setter
    def private_attr(self, value):
        self.__private_attr = value


obj = Example("Public", "Protected", "Private")

# Public Attribute
print(obj.public_attr)  # Uses getter, Output: PUBLIC
obj.public_attr = "new value"  # Setter logic, Output: NEW VALUE

# Protected Attribute
print(obj.protected_attr)  # no need to use _ ,  Output: Protected
obj.protected_attr = "new protected value"  # Directly updates value

# Private Attribute
print(obj.private_attr)  # no need to use __ , Output: Private
obj.private_attr = "new private value"  # Uses setter

# Attempt direct access
# print(obj.__private_attr)  # Error! Private attribute
# Access possible via mangling:
print(obj._Example__private_attr)  # Not recommended


"""
The @property decorator essentially makes protected (_attr) or private (__attr) attributes behave as if they are public attributes when accessed through the getter and setter methods.

How @property Changes Behavior
    Normally, protected or private attributes would require explicit access (obj._protected_attr or obj._ClassName__private_attr).
    With @property, you define a public-facing interface for the attribute while hiding the actual implementation (e.g., storing the value in a protected or private variable).
    The user of the class can interact with the attribute as if it were public, without worrying about whether it’s actually protected or private.

Why Does This Happen?
    When you define a property using the @property decorator:

    Getter Method: Replaces the direct access to the attribute. When you call obj.attr, Python invokes the getter method instead.
    Setter Method: Replaces the direct assignment to the attribute. When you assign obj.attr = value, Python invokes the setter method.
"""


"""
Key Takeaways

    Public Attributes:
        Directly accessible without @property.
        Use @property to add logic for getting/setting.

    Protected Attributes:
        Accessible but intended for internal use (_attr).
        Use @property to better manage access.

    Private Attributes:
        Not accessible directly from outside the class due to name mangling.
        Must be accessed or modified using @property or other public methods.
"""