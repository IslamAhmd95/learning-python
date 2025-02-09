"""
What is an Enum?
An Enum (short for enumeration) is a class in Python that is used to define a set of constant values, often representing options or categories. It provides a way to group related values together with names instead of using raw values like integers or strings directly.

In Python, enums are part of the enum module, introduced in Python 3.4.

Creating an Enum
To create an Enum in Python, you need to use the Enum class from the enum module.
"""

from enum import Enum, unique, auto


# example
class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

print(Day)  # <enum 'Day'>
print(repr(Day))  # <enum 'Day'>
print(type(Day))  # <class 'enum.EnumType'>
print(list(Day))  # [<Day.MONDAY: 1>, <Day.TUESDAY: 2>, <Day.WEDNESDAY: 3>, <Day.THURSDAY: 4>, <Day.FRIDAY: 5>, <Day.SATURDAY: 6>, <Day.SUNDAY: 7>]
print(Day.MONDAY)  # Day.MONDAY
print(Day.MONDAY.name)  # MONDAY
print(Day['MONDAY'].name) # MONDAY
print(Day.MONDAY.value)  # 1
print(Day['MONDAY'].value)  # 1

for day in Day:
    print(day)  # Day.MONDAY Day.TUESDAY Day.WEDNESDAY Day.THURSDAY DAY.FRIDAY Day.SATURDAY Day.SUNDAY


# example
class Color(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"

print(Color.RED)  # COLOR.RED
print(Color.RED.name)  # RED
print(Color.RED.value)  # Red

for color in Color:
    print(color)  # COLOR.RED COLOR.GREEN COLOR.BLUE


#----------------------------------------------------------------


"""
Enum Member Comparison:

    Enum members are compared using their values by default.Identity in Python means whether two variables or objects refer to the exact same object in memory.
    The is operator checks identity.

    Enum members are unique by identity.
        Each Enum member is treated as a singleton. Even if two members share the same value (due to aliases), they still refer to the same object in memory.
        This means two Enum members with the same value are not separate objects but actually refer to the same member.
    
    If two members have the same value, they are considered aliases of the same member, and comparisons reflect this.

    # Comparison by identity
    print(Status.ACTIVE is Status.TEST)  # True (they are the same object)
    print(Status.ACTIVE == Status.TEST)  # True (same value and same object)

    # Comparison by value
    print(Status.ACTIVE.value == Status.TEST.value)  # True (value is 1 for both)

    
    What Is Identity in Python?
        Identity refers to the unique existence of an object in memory.
        Every object in Python has a unique identifier, which you can check using the id() function.
        The is operator checks whether two variables point to the same object in memory.

        Example of identity:
        x = [1, 2, 3]
        y = x  # Both x and y point to the same object
        z = [1, 2, 3]  # A new list with the same content as x

        print(x is y)  # True, because x and y refer to the same object
        print(x is z)  # False, because z is a different object in memory


    What Does It Mean for Two Objects to Be the "Same Object"?
        If two variables or names point to the exact same location in memory, they are considered the same object.

        Practical Implications:
            Modifying one will affect the other because they both point to the same data in memory.
            If two variables are the same object, is returns True, and their id() values are the same.

    Difference Between Equality (==) and Identity (is)
        Equality (==) checks if two objects have the same value.
        Identity (is) checks if two objects are the same object in memory.

"""
# @unique
class Status(Enum):
    ACTIVE = 1
    TEST = 1  # if we uncommented @unique decorator of enum module, this error will be raised "ValueError: duplicate values found in <enum 'Status'>: TEST -> ACTIVE"
    INACTIVE = 2
    PENDING = 3

print(Status.ACTIVE == Status.INACTIVE)  # False
print(Status.ACTIVE == Status.ACTIVE)  # True
print(Status.TEST)   # Status.ACTIVE
"""
print(Status.TEST)   # Status.ACTIVE
Why Does This Happen?

    Enum Values Must Be Unique:
        Python's Enum enforces uniqueness among its members' values.
        If two or more members have the same value, the first member with that value takes precedence, and the others are treated as aliases (alternative names) for the same member.

    Aliases in Enums:
        Status.TEST is treated as an alias for Status.ACTIVE because both have the same value (1), and Status.ACTIVE appears first.

How to Avoid Aliases
    If you want to prevent aliases and enforce unique values for all members, use the @unique decorator from the enum module.
"""
# List all members, including aliases
print(Status.__members__)  # {'ACTIVE': <Status.ACTIVE: 1>, 'TEST': <Status.ACTIVE: 1>, 'INACTIVE': <Status.INACTIVE: 2>, 'PENDING': <Status.PENDING: 3>}

# List all members without aliases
print(list(Status)) # [<Status.ACTIVE: 1>, <Status.INACTIVE: 2>, <Status.PENDING: 3>]


#----------------------------------------------------------------

"""
Auto-Assigning Values with auto()
    If you don't want to manually assign values to enum members, you can use the auto() function, which automatically assigns sequential integer values starting from 1.
"""

class Numbers(Enum):
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()


print(Numbers.ONE, Numbers.TWO)  # Numbers.ONE Numbers.TWO
print(Numbers.ONE.value, Numbers.TWO.value)  # 1  2

#----------------------------------------------------------------

"""
Enum with Methods
    You can also define methods within an enum class, allowing the enum members to have custom behaviors.
"""

class Animals(Enum):
    CAT = "CAT"
    DOG = "DOG"

    def sound(self):
        if self == Animals.CAT:
            return "Meow!"
        elif self == Animals.DOG:
            return "Woof!"
        

print(Animals.CAT.sound())  # Meow!
print(Animals.DOG.sound())  # Woof!

"""
Animals.CAT as an Object
    In the class Animals, each Enum member (e.g., Animals.CAT, Animals.DOG) is a unique object.
    When you call a method like sound() on Animals.CAT, Python internally passes that Enum member (Animals.CAT) as the value of self.

How self Works
    In Python, the first parameter of a class method (self) always refers to the instance (or object) that is calling the method.
    Here, when Animals.CAT.sound() is called:
    self refers to the object Animals.CAT.
"""

#----------------------------------------------------------------


# example:
class UserRole(Enum):
    ADMIN = "Admin"
    USER = "User"
    GUEST = "Guest"


def check_role(role):
    if role == UserRole.ADMIN:  # role == UserRole.ADMIN is better than using rol == UserRole.ADMIN.value, Code should depend on structure (the Enum), not specific string values.
        return "You are an administrator."
    elif role == UserRole.USER:
        return "You are a user."
    elif role == UserRole.GUEST:
        return "You are a guest."

# Simulate dynamic role assignment (e.g., from user input or database)
user_input = "Admin"  
# user_input = "Administrator" 
try:
    # Convert input value to the corresponding Enum member
    role = UserRole(user_input)
    print(check_role(role))  # Pass the Enum member to the function
except ValueError:
    print("Invalid role.")




# example:

class Status(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

status = Status.ACTIVE

# Works now
if status.value == "Active":
    print("Account is active.")

# If the value changes later
class Status(Enum):
    ACTIVE = "Actv"  # Typo or deliberate change

if status.value == "Active":  # This will fail silently
    print("Account is active.")
# By comparing status == Status.ACTIVE, you don't rely on the value and avoid potential problems if the value changes.




# example:

class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4

# Example usage
def log(message, level):
    if level == LogLevel.ERROR:
        print(f"ERROR: {message}")
    elif level == LogLevel.WARNING:
        print(f"WARNING: {message}")

log("This is a warning.", LogLevel.WARNING)
