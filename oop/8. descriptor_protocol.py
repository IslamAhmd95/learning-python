"""
Python's Descriptor Protocol Explained
In Python, descriptors are a way to customize how attributes of a class are accessed or modified. They allow you to control what happens when you get, set, or delete an attribute.


Basic Idea
    If an object defines any of these methods:
        __get__(self, instance, owner) → For getting an attribute.
        __set__(self, instance, value) → For setting an attribute.
        __delete__(self, instance) → For deleting an attribute.
    Then, it becomes a descriptor.

    
Why Use Descriptors?
    Descriptors are useful when you want to:
        Validate data before assigning it.
        Manage how data is stored or accessed.
        Implement computed properties.

         
Types of Descriptors
    Data Descriptors
        If a class defines both __get__ and __set__, it’s a data descriptor.
        → They control both reading and writing of an attribute.

    Non-Data Descriptors
        If a class only defines __get__, it’s a non-data descriptor.
        → They only control reading.

        
When to Use Descriptors?
    Validation – Ensure data correctness (like positive numbers).
    Computed Properties – Dynamically calculate values.
    Lazy Loading – Load data when accessed, not during initialization.
    Resource Management – Control how resources (files, DB connections) are accessed.
"""


# 1. Data Descriptor (with __get__ and __set__)
class PositiveNumber:
    def __get__(self, instance, owner):
        # Return the protected internal value
        return instance._positive_number_value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Price must be positive.")
        # Set the protected internal value
        instance._positive_number_value = value  # "_positive_number_value" must match the same name in get method


class Product:
    price = PositiveNumber()  # This links to the descriptor

    def __init__(self, name, price):
        self.name = name
        self.price = price  # Triggers the __set__ method of the descriptor


product = Product("Glasses", 30)
print(product.price)  # 30

try:
    product.price = -10
except ValueError as e:
    print(e)  # Price must be positive.

product.price = 50
print(product.price)  # 50
"""
- PositiveNumber controls how price is set.
- If a negative value is set, it raises an error.
- Reading price triggers __get__.
- Always use a protected attribute inside the descriptor to store the value. This prevents external code from directly modifying it.
- Rename internal attributes in the descriptor to something more unique (e.g., _positive_number_value) to avoid confusion with the public attribute (price in Product).
- Public attributes in your class (like price in Product) should interact with descriptors, but the actual data should remain protected within the descriptor.
- The main reason to rename them differently is to avoid confusion and name clashes. By giving the descriptor's internal attribute a unique name (_positive_number_value), you make it clear that it is a separate entity and should not be directly accessed.
"""



# 2. Non-Data Descriptor (with only __get__)
class UpperCaseDescriptor:
    def __get__(self, instance, owner):
        """
        Convert the stored value in `_raw_name` to uppercase.
        This method is triggered when `user._raw_name` is accessed.
        - `instance`: The instance of the User class (e.g., `user`).
        - `owner`: The class of the instance (e.g., User).
        """
        return instance._raw_name.upper() # Access and convert the protected attribute to uppercase


class User:
    # Bind the descriptor to a class-level attribute
    display_name = UpperCaseDescriptor()

    def __init__(self, name):
        """
        `name` is the input provided when creating an instance.
        `_raw_name` is a protected attribute used internally for storage.
        """
        self._raw_name = name


# Example usage
user = User("john")

# Access the descriptor (triggers UpperCaseDescriptor.__get__)
print(user.display_name)  # Output: JOHN

# Directly access the raw stored value
print(user._raw_name)  # Output: john
"""
How It Works in the Code:

Initialization:
    user = User("john")
    The User class constructor (__init__) sets self._raw_name = name, where name is "john".
    _raw_name now holds the raw, unprocessed value "john".

Accessing display_name:
    print(user.display_name)  # Output: JOHN
    When user.display_name is accessed, Python:
        Detects that display_name is a descriptor.
        Calls UpperCaseDescriptor.__get__, passing user as the instance and User as the owner.
        The __get__ method retrieves the value of user._raw_name ("john") and converts it to uppercase, returning "JOHN".

Accessing _raw_name directly:
    print(user._raw_name)  # Output: john
    Accessing _raw_name bypasses the descriptor and retrieves the raw stored value directly.


Advantages of the Enhanced Version:
    Separation of Concerns:
        _raw_name is strictly for storage.
        display_name provides controlled, processed access through the descriptor.
    Encapsulation:
        The logic for processing the name (e.g., converting to uppercase) is encapsulated in UpperCaseDescriptor.
        This ensures consistency and allows easy reuse in other contexts.
    Clarity:
        The use of _raw_name (protected) and display_name (public interface) makes the intent clear: _raw_name stores raw data, and display_name provides a formatted view.


Key Points Explained

1. Why _raw_name and not display_name in User:
    If you directly used self.display_name = name in the __init__ method:
        Python would bypass the UpperCaseDescriptor because instance-level attributes override class-level descriptors.
        Assigning the raw value to a different name (e.g., _raw_name) avoids this conflict and ensures that the UpperCaseDescriptor can manage access to display_name.
2. The role of display_name in User:
    display_name is a class-level attribute bound to the UpperCaseDescriptor.
    When you access user.display_name, Python calls the __get__ method of UpperCaseDescriptor, which retrieves the raw value stored in _raw_name, converts it to uppercase, and returns it.
3. The role of _raw_name in User:
    _raw_name is an instance-level attribute used to store the original (raw) value passed during initialization.
    It is protected (indicated by the _ prefix) to signal that it is an internal implementation detail and should not be accessed or modified directly by external code.
    However, it is still accessible directly if needed (e.g., user._raw_name).
4. Why use UpperCaseDescriptor:
    It encapsulates the logic of converting a string to uppercase when accessed via display_name.
    The descriptor ensures consistent behavior for all instances of the User class and can also be reused in other classes where similar functionality is required.

    
When using the __get__ method of a descriptor, the attribute name (_raw_name in this case) must match the actual attribute name used in the instance. However, when using __set__, the names can differ.
Why?
    With __get__:
        The descriptor reads from the instance but doesn't control attribute names. It must look for an attribute that already exists in the instance.
    With __set__:
        The descriptor writes to the instance and has complete control over how and where the data is stored. It can dynamically create or update attributes with any name.

"""
"""
1. Non-Data Descriptor (Only __get__)
    A descriptor with only the __get__ method is called a non-data descriptor.
    In this case, no __set__ exists to control assignment, so the descriptor only manages attribute retrieval.
    The instance attribute accessed in __get__ must exactly match the attribute name used in the instance.
    ✅ Best Practice:
        The internal attribute should be protected (prefixed with _) to avoid accidental access or modification.
    Example:
        class UpperCase:
            def __get__(self, instance, owner):
                return instance._name.upper()  # Must match instance attribute

        class User:
            name = UpperCase()  # Descriptor

            def __init__(self, name):
                self._name = name  # Must be '_name' to match the descriptor

        user = User("john")
        print(user.name)   # Output: JOHN
        print(user._name)  # Output: john
        # If you used self.name = name instead of self._name, the descriptor would be bypassed, and user.name would return the raw string.


2. Data Descriptor (__get__ and __set__)
    A descriptor with both __get__ and __set__ is called a data descriptor.
    Since __set__ intercepts assignments, the descriptor can control how values are stored in the instance.
    The attribute used in both __get__ and __set__ must be the same to keep the data flow consistent.
    ✅ Best Practice:
        Use a protected attribute for internal storage to avoid accidental modification.
    Example:
        class PositiveNumber:
            def __get__(self, instance, owner):
                return instance._positive_number_value  # Same name as in __set__

            def __set__(self, instance, value):
                if value < 0:
                    raise ValueError("Value must be positive.")
                instance._positive_number_value = value  # Same as in __get__

        class Product:
            price = PositiveNumber()

            def __init__(self, price):
                self.price = price  # Triggers __set__

        product = Product(50)
        print(product.price)  # Output: 50

        product.price = 100   # Triggers __set__
        print(product.price)  # Output: 100

        try:
            product.price = -10  # Raises ValueError
        except ValueError as e:
            print(e)  # Output: Value must be positive.
        # __set__ gives full control over how the value is stored, so the internal attribute (_positive_number_value) can be anything, as long as it matches between __get__ and __set__.
        # If the names don't match, __get__ won't retrieve the correct value.


Problem with Non-Data Descriptors
    In a non-data descriptor (with only __get__), if you assign directly to a public attribute in the instance, it will override the descriptor.
    ❌ Incorrect Approach
        class UpperCase:
            def __get__(self, instance, owner):
                return instance._name.upper()

        class User:
            name = UpperCase()  # Non-data descriptor

            def __init__(self, name):
                self.name = name  # ❌ This overrides the descriptor!

        user = User("john")
        print(user.name)  # Output: john  (Descriptor is bypassed!)
        # Here, self.name = name overrides the name descriptor because the assignment creates an instance-level attribute.
        # Descriptors work on class attributes, but instance attributes take priority.

    ✅ Correct Approach: Public Access with Protected Storage
    You can keep name public while storing the actual value in a protected attribute internally.
        class UpperCase:
            def __get__(self, instance, owner):
                return instance._name.upper()  # Accesses the protected attribute

        class User:
            name = UpperCase()  # Descriptor remains public

            def __init__(self, name):
                self._name = name  # ✅ Use protected storage

        user = User("john")
        print(user.name)  # Output: JOHN  (Descriptor works!)
        print(user._name)  # Output: john  (Raw value)
        # name is a public attribute because it’s bound to the UpperCase descriptor.
        # The actual value is stored in _name (protected), so it doesn’t override the descriptor.
        # Accessing user.name triggers the descriptor (__get__), returning the uppercase version.

"""

# example: Real-Life Example: Type Checking
class Integer:
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Value must be an integer')
        instance._value = value
    
    def __get__(self, instance, owner):
        return instance._value
    

class Person:
    age = Integer()

    def __init__(self, age):
        self.age = age

person = Person(20)

try:
    person = Person("twenty")
except TypeError as e:
    print(e)   # Value must be an integer

print(person.age)  # 20


"""
Descriptors (__get__, __set__) → Best for reusing validation across multiple classes but typically handle one attribute per descriptor.
@property → Convenient for handling multiple attributes in the same class, but not reusable across classes.
"""

# __delete__ allows you to control what happens when an attribute is deleted using the del statement.

# Example: Resetting a Value on Delete
class ResetOnDelete:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        instance._value = value

    def __delete__(self, instance):
        print("Value has been deleted. Resetting to 0.")
        instance._value = 0  # Reset instead of deleting

class Item:
    price = ResetOnDelete()

    def __init__(self, price):
        self.price = price

# Usage
item = Item(100)
print(item.price)  # Output: 100

del item.price      # Triggers __delete__, resets to 0
print(item.price)   # Output: 0


# Example: Ensuring a value stays within a specific range (e.g., between 0 and 100):
class Range:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __get__(self, instance, owner):
        return instance._value
    
    def __set__(self, instance, value):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Value must be between {self.min_value} and {self.max_value}")
        instance._value = value

class Temperature:
    degree = Range(-50, 50)

    def __init__(self, degree):
        self.degree = degree


# Usage
temperature = Temperature(20)
print(temperature.degree)  # Output: 20

try:
    temperature.degree = 100  # Raises ValueError
except ValueError as e:
    print(e)  # Value must be between -50 and 50



# Example: Automatically converts assigned values to a specific type (e.g., string):

class Stringfy:
    def __get__(self, instance, owner):
        return instance._value
    
    def __set__(self, instance, value):
        instance._value = str(value)
    
class Value:
    value = Stringfy()

    def __init__(self, value):
        self.value = value


# Usage
obj = Value(100)
print(type(obj.value))  # Output: <class 'str'>

obj.value = 200  
print(type(obj.value))  # Output: <class 'str'>



# Example: Simulate removing sensitive data like passwords:
class SecureAttribute:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        instance._value = value

    def __delete__(self, instance):
        print("Sensitive data has been deleted.")
        instance._value = None  # Nullify the sensitive data

class User:
    password = SecureAttribute()

    def __init__(self, password):
        self.password = password

# Usage
user = User("my_secret")
print(user.password)  # Output: my_secret

del user.password     # Triggers __delete__
print(user.password)  # Output: None



"""
In descriptor methods like __get__ and __set__, the parameters have specific roles:
    self → Refers to the descriptor instance itself.
        It's the object of the descriptor class (e.g., Range, Stringify).
        Used to access the descriptor’s own attributes or methods.
    instance → The object of the class where the descriptor is used.
        It’s the actual object that owns the attribute being accessed or modified.
        None when accessed via the class instead of an instance.
    owner → The class where the descriptor is defined.
        It refers to the class itself, not an instance.
        Helps if you need to access class-level data or behavior.
"""
# Example Demonstrating self, instance, and owner
class DescriptorExample:
    def __get__(self, instance, owner):
        print(f"self: {self}")       # Descriptor instance
        print(f"instance: {instance}")  # Object of the class where descriptor is used
        print(f"owner: {owner}")     # Class itself
        return 42

class MyClass:
    attr = DescriptorExample()  # Descriptor attached to 'attr'

# Access through an instance
obj = MyClass()
print(obj.attr)

# Access through the class "owner"
print(MyClass.attr)
"""
Output:
    self: <__main__.DescriptorExample object at 0x...>
    instance: <__main__.MyClass object at 0x...>
    owner: <class '__main__.MyClass'>
    42
    self: <__main__.DescriptorExample object at 0x...>
    instance: None  # because we called the attribute with the class "the owner" instead of the instance "the object"
    owner: <class '__main__.MyClass'>
    42
"""


"""
Why Use Protected Attributes (_value) in Descriptors?
Encapsulation
    Using _value makes the attribute protected, signaling that it should not be accessed directly.
    This prevents users from bypassing the descriptor logic.
Avoid Naming Conflicts
    If we used instance.value, it would conflict with the descriptor itself (value = Descriptor()).
    _value keeps internal storage separate.
Data Safety
    By convention, leading underscores (_) tell other developers:
    → "This is internal. Don’t touch it!"

    
❌ Without Using a Protected Attribute:
class BadDescriptor:
    def __set__(self, instance, value):
        instance.value = value  # This calls the descriptor again and causes infinite recursion!

class Test:
    value = BadDescriptor()

obj = Test()
# obj.value = 10  # This will cause a RecursionError!

Why This Fails:
    obj.value = 10 triggers BadDescriptor.__set__.
    Inside __set__, instance.value = value is called.
    But value is still controlled by the descriptor → So __set__ is triggered again!
    This repeats forever, causing infinite recursion → RecursionError.

    
✅ With Protected Attribute:
class GoodDescriptor:
    def __set__(self, instance, value):
        instance._value = value  # Safe storage, Storing in _value avoids recursion and keeps data safe.

    def __get__(self, instance, owner):
        return instance._value

class Test:
    value = GoodDescriptor()

obj = Test()
obj.value = 10
print(obj.value)  # Output: 10

Why This Works:
    obj.value = 10 calls __set__.
    Inside __set__, it sets instance._value = value.
    _value is not managed by the descriptor, so no recursion happens.

How to Avoid Recursion
    You must use a different attribute name that the descriptor is not managing.
    It can be protected (_value) which is more recommended or public (custom_name), as long as it's not the same as the descriptor.

✅ Using a Different Public Attribute (No Recursion)
class Descriptor:
    def __set__(self, instance, value):
        instance.actual_value = value  # ✅ Different public attribute

    def __get__(self, instance, owner):
        return instance.actual_value

class MyClass:
    value = Descriptor()

obj = MyClass()
obj.value = 10  # No recursion
print(obj.value)  # Output: 10

Why This Works:
    value is managed by the descriptor.
    actual_value is a different attribute, so no recursion occurs.
    actual_value is public, and it still works.

    
✅ Using a Protected Attribute (Recommended)
class Descriptor:
    def __set__(self, instance, value):
        instance._value = value  # ✅ Protected but safe

    def __get__(self, instance, owner):
        return instance._value

class MyClass:
    value = Descriptor()

obj = MyClass()
obj.value = 20
print(obj.value)  # Output: 20

Why This is Better:
    Protected (_value) suggests it’s for internal use.
    Other developers know not to touch _value directly.
"""