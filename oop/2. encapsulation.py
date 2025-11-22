"""
Encapsulation in Python
Encapsulation is one of the key principles of Object-Oriented Programming (OOP). It focuses on hiding implementation details and exposing only necessary parts of a class. This is achieved using access modifiers to control how data and methods are accessed and modified.


Access Modifiers in Python
In Python, access modifiers are implemented using naming conventions:

Public: Accessible from anywhere.
    Attributes and methods are public by default.
    No special prefix is required.
Protected: Suggests limited access, meant to be used within the class and its subclasses.
    Prefix with a single underscore _.
Private: Restricted access, meant to be used only within the class.
    Prefix with double underscores __.
"""
class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder   # Public attribute
        self._balance = initial_balance   # Protected attribute
        self.__pin = "1234"   # private attribute

    # public method
    def get_balance(self):
        return self._balance
    
    # protected method
    def _update_balance(self, amount):
        self._balance += amount

    # private method
    def __validate_pin(self, pin):
        return self.__pin == pin
    
    # public method demonstrating encapsulation
    # It focuses on hiding implementation details and exposing only necessary parts of a class. This is achieved using access modifiers to control how data and methods are accessed and modified.
    def withdraw(self, amount, pin):
        if self.__validate_pin(pin):
            if amount > self._balance:
                print("Insufficient funds")
            else:
                self._update_balance(-amount)
                print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Invalid PIN")

    # public method demonstrating encapsulation
    # It focuses on hiding implementation details and exposing only necessary parts of a class. This is achieved using access modifiers to control how data and methods are accessed and modified.
    def deposit(self, amount, pin):
        if self.__validate_pin(pin):
            self._update_balance(amount)
            print(f"Deposit {amount}. New balance: {self._balance}")
        else:
            print("Invalid PIN")


account = BankAccount("Islam", 1000)
print(account.account_holder)  # Islam
print(account.get_balance())  # 1000
account.withdraw(500, "1234") # Withdrew 500. New balance: 500
account.withdraw(500, "123")  # Invalid PIN
account.withdraw(5000, "1234")  # Insufficient funds
account.deposit(500, "123")  # Invalid PIN
account.deposit(500, "1234")  # Deposit 500. New balance: 1000

# Access private attribute (will cause an error)
# print(account.__pin)  # AttributeError

# Try accessing private method (will cause an error)
# account.__validate_pin("1234")  # AttributeError

"""
Key Points About Encapsulation

Public Attributes and Methods:
    Accessible from outside the class.
    Typically used for general-purpose interactions with the class.
    Example: account.account_holder or account.get_balance().

Protected Attributes and Methods:
    Conventionally accessed only within the class and its subclasses.
    Not strictly enforced, but the _ prefix serves as a warning to other developers.
    Example: account._balance.

Private Attributes and Methods:
    Can only be accessed within the class.
    Enforced by Python using name mangling "explained below": private attributes are internally renamed (e.g., __pin becomes _BankAccount__pin).
    Example: account.__pin

    
Why Use Encapsulation?
    Data Hiding:
        Prevents accidental modification of sensitive data.
    Controlled Access:
        Provides controlled access through getter and setter methods.
    Improved Maintainability:
        Implementation details can be changed without affecting external code.    
"""

#----------------------------------------------------------------

"""
In Python, name mangling is a mechanism used to enforce some level of protection for private attributes and methods in a class. When an attribute is defined with a double underscore prefix (e.g., __attribute), Python automatically changes its name internally to make it harder to accidentally override or access from outside the class.
This internal renaming is called name mangling, and it adds a _ClassName prefix to the attribute name.

What Does Name Mangling Do?
    When you define a private attribute or method with double underscores (__), Python translates it behind the scenes to a new name:
    __attribute becomes _ClassName__attribute.
    This makes it more challenging for external code to accidentally or intentionally access these private members, although it does not make them completely inaccessible.

Why Does Python Use Name Mangling?
    Prevent Name Collisions:
        When a class is extended (via inheritance), name mangling prevents subclasses from accidentally overriding private attributes or methods of the parent class.
    Encapsulation:
        Name mangling encourages better coding practices by discouraging direct access to private attributes and methods.

Important Notes
    Name mangling is not true access restriction:
        It is more of a discouragement than a strict enforcement.
        You can still access private members using their mangled names.
    Single Underscore (_) is not name mangling:
        Attributes with a single underscore are considered "protected" by convention but are not name-mangled.
"""


# Example of name mangling with Inheritance  
class Parent:
    def __init__(self):
        self.__private_attr = "I am private in this parent class"

    def access_private_attr(self):
        return self.__private_attr


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__private_attr = "I am private in this child class"

child = Child()

# Access the private attribute of the Parent class via its method
print(child.access_private_attr())  # I am private in this parent class

# Access the private attribute of the Child class via name mangling
print(child._Child__private_attr)  # I am private in this child class



# Example with Name Mangling
class Example:
    def __init__(self):
        self.__private_attr = "I am a private attribute"

    def __private_method(self):
        return "This is a private method"

    def access_private_method(self):
        return self.__private_method()

# Create an instance of the class
obj = Example()

# Try to access the private attribute directly (this will fail)
# print(obj.__private_attr)  # AttributeError

# Try to access the private method directly (this will fail)
# print(obj.__private_method())  # AttributeError

# Access the private attribute using the mangled name "not recommended"
print(obj._Example__private_attr)  # Output: I am a private attribute

# Access the private method using the mangled name "not recommended"
print(obj._Example__private_method())  # Output: This is a private method

# Access the private method via a public method "recommended"
print(obj.access_private_method())  # Output: This is a private method

"""
How Name Mangling Works in the previous example
    - When __private_attr is defined, Python renames it internally to _Example__private_attr.
    - Similarly, the method __private_method is renamed to _Example__private_method.
    - External code cannot directly access __private_attr or __private_method because they are no longer recognized under those names.
    - The mangled names (_Example__private_attr and _Example__private_method) can still be used, but they are less convenient and meant to discourage direct access.

    
Accessing Private Attributes or Methods

    Name Mangling Access (First 2 Prints of the last example):
        Accessing private attributes or methods using their mangled names (e.g., _ClassName__attribute) is possible but not recommended.
        This breaks the encapsulation principle and should be avoided unless absolutely necessary (e.g., debugging or rare edge cases).

    Public Methods for Access (Third Print):
        The best practice is to use public methods inside the class to access or modify private attributes.
        Public methods can include getters and setters, which are common patterns for controlled access.

    Private Access in Subclasses:
        Private attributes and methods cannot be directly accessed in subclasses because they are mangled with the parent class's name "_className__privateAttr".
        This is intentional to avoid conflicts and enforce encapsulation.
"""


"""
Modifying Private Attributes Using Name Mangling
    Yes, you can modify private attributes using name mangling. However, this is not recommended because it bypasses any validation logic in setters or public methods.
"""
class Example:
    def __init__(self):
        self.__private_attr = "I am private"

obj = Example()

# Access and modify the private attribute via name mangling
print(obj._Example__private_attr)  # Output: I am private
obj._Example__private_attr = "Modified private attribute"
print(obj._Example__private_attr)  # Output: Modified private attribute


"""
Modifying Private Methods
    Private methods cannot be directly modified because methods are functions and not variables. However, you can override the behavior of private methods by redefining them in the same class or subclass.

    If you try to access a private method using name mangling, it can still be called (invoked) but not directly changed:
"""
class Example:
    def __private_method(self):
        return "Private method"

# Accessing the private method using name mangling
obj = Example()
print(obj._Example__private_method())  # Output: Private method

# Attempting to modify the private method
# This would require redefining or overriding it


"""
Key Takeaways

    Best Practices:
        Use public methods (like getters and setters) to interact with private attributes and methods.
        Avoid using name mangling directly in normal circumstances.

    Private in Subclasses:
        Private attributes and methods are inaccessible in subclasses due to name mangling.
        Subclasses should use public or protected methods/attributes from the parent class.

    Name Mangling:
        Allows accessing and modifying private attributes but not private methods.
        Modifying private attributes via name mangling is possible but strongly discouraged.
"""

#-----------------------------------------------------------------------------------------

"""
Protected attributes (attributes prefixed with a single underscore, _attr) are designed with a specific intent:

    Not for Direct External Access:
        Protected attributes signal that they are intended for internal use within the class or its subclasses.
        While technically accessible outside the class (e.g., obj._protected_attr), it is not recommended as it breaks encapsulation and can lead to fragile code.
    Intended Use in Subclasses:
        The main purpose of protected attributes is to make them accessible in subclasses while still discouraging direct access from outside the class hierarchy.
    Best Practice:
        Access or modify them using getters, setters, or other public methods of the class if needed externally.
        Subclasses can directly use them as part of their internal implementation.
"""

class Parent:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def get_name(self):
        return self._name.capitalize()  # Public method for external use


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self._age = age  # Another protected attribute

    def display_info(self):
        # Accessing protected attributes in the subclass
        return f"Name: {self._name}, Age: {self._age}"


# Usage
child = Child("john", 10)

# Access protected attribute through public method "recommended"
print(child.get_name())  # Output: John

# Accessing protected attribute directly (not recommended)
print(child._name)  # Output: john

# Accessing protected attribute from within the subclass (recommended)
print(child.display_info())  # Output: Name: john, Age: 10
