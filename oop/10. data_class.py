"""
A data class is a special kind of class in Python designed to store data. Instead of writing a lot of repetitive code to define __init__, __repr__, and other methods, Python can generate them for you automatically using the @dataclass decorator.

Why Use Data Classes?
    When your class is mostly about storing data (e.g., user profiles, coordinates, etc.), you don’t want to waste time writing:
        An initializer (__init__) to set up attributes.
        A string representation (__repr__) to display the class nicely.
        Equality checks (__eq__) to compare two instances.
"""
from dataclasses import dataclass, field

# instead of this
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


# we do this
@dataclass
class Point:
    x: int   # attributes without default values must be declared first
    y: int = 0

p1 = Point(10, 20)  # Automatically creates a Point instance with x=10 and y=20
p2 = Point(10, 20)

# Access attributes
print(p1.x)  # Output: 10

# Auto-generated __repr__ for nice output
print(p1)  # Output: Point(x=10, y=20)

# Auto-generated __eq__ for comparisons
print(p1 == p2)  # Output: True (compares attribute values, not memory addresses)

"""
How It Works
    @dataclass Decorator: Tells Python to automatically add common methods like __init__ and __repr__.
    Attributes: You list them with their types (int, str, etc.), and Python uses these to create methods.
"""


# We can add default values to the attributes
@dataclass
class Point:
    x: int = 0
    y: int = 0

p1 = Point()         # Uses default values (x=0, y=0)
p2 = Point(10, 20)   # Overrides defaults with x=10, y=20

print(p1)  # Output: Point(x=0, y=0)
print(p2)  # Output: Point(x=10, y=20)



"""
Handling Advanced Cases with field
    The field() function gives extra control. For example:
        Using default values for mutable attributes.
        Hiding an attribute from methods like __repr__.
"""
@dataclass
class Student:
    name : str
    grades : list = field(default_factory=list)  # # Creates a new list for each student

s1 = Student("Alice")
s2 = Student("Bob")

s1.name = "John"
s1.grades.append(85)  # Modifying a list in s1's instance
print(s1.name)  # Output: "John"
print(s1.grades)  # Output: [85]
print(s1)   # Output: Student(name='John', grades=[85])
print(s2.grades)  # Output: [] (since s2's instance has its own list and it's empty)



"""
Making Data Classes Read-Only (Immutable)
    If you want a class to behave like a constant (where attributes cannot be changed), use frozen=True:
"""
@dataclass(frozen=True)
class Color:
    red: int
    green: int
    blue: int


c = Color(255, 0, 0)
print(c.red)  # Output: 255
# c.red = 128  # This will raise an error: cannot assign to field 'red'


"""
Post-Initialization Processing
    Sometimes you need to calculate values after all attributes are set. Use __post_init__ for that:
"""
@dataclass
class Person:
    name: str
    age : int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age must be a positive integer.")
        

try:
    person = Person("ahmed", -17)
    print(person.name)
except ValueError as e:
    print(f"Error: {e}")


@dataclass
class Rectangle:
    width : float
    height : float
    area : float = field(init=False)  # Excluded from __init__

    def __post_init__(self):   
        self.area = self.width * self.height


r = Rectangle(3, 4)
print(r.area)  # Output: 12


"""
Adding Comparison Methods
    By default, data classes generate __eq__ for equality. To add ordering methods (<, >, etc.), use order=True:

What Does order=True Do?
    Adding order=True generates comparison methods (<, <=, >, >=) in addition to eq.
    These methods compare objects based on the order of their fields.
    Without order=True, attempting to use these operators (<, >, etc.) will raise a TypeError.
"""
@dataclass(order=True)
class Student:
    name : str
    grade : int

s1 = Student("Alice", 85)
s2 = Student("Bob", 90)
print(s1 > s2)  # False
print(s1 < s2)  # True



"""
Can Data Classes Have Methods?
    Absolutely! Data classes can have any methods, just like normal classes. The @dataclass decorator doesn't stop you from adding your own methods; it only helps with generating boilerplate code like __init__, __repr__, etc.
"""

@dataclass
class Circle:
    radius: float

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def circumference(self) -> float:
        return 2 * 3.14159 * self.radius

c = Circle(5)
print(c.area())           # Output: 78.53975
print(c.circumference())  # Output: 31.4159



"""
What is the Use of default_factory?
    default_factory is used to provide a default value for mutable types like lists, dictionaries, or sets. It solves a common bug where all instances of a class share the same mutable default object.

# Without default_factory (Buggy Behavior)
    @dataclass
    class Student:
        name: str
        grades: list = []  # BAD: All instances share this list and will produce an error "ValueError: mutable default <class 'list'> for field grades is not allowed: use default_factory"

    s1 = Student("Alice")
    s2 = Student("Bob")

    # s1.grades.append(90)
    # print(s1.grades)  # Output: [90]
    # print(s2.grades)  # Output: [90] (BUG: Shared list!)


# Using default_factory (Correct Behavior)
    @dataclass
    class Student:
        name: str
        grades: list = field(default_factory=list)  # field(default_factory=list) ensures that each instance gets a new list instead of sharing one.

    s1 = Student("Alice")
    s2 = Student("Bob")

    s1.grades.append(90)
    print(s1.grades)  # Output: [90]
    print(s2.grades)  # Output: [] (Separate list!)
"""



"""
Inheritance
    Data classes support inheritance, just like normal classes. You can even add or override fields and methods in subclasses.
"""
@dataclass
class Animal:
    name: str

@dataclass
class Dog(Animal):
    breed: str

dog = Dog("Buddy", "Golden Retriever")
print(dog)  # # Output: Dog(name='Buddy', breed='Golden Retriever')



"""
Class Variables
    Use field(init=False) for attributes that aren't part of __init__.

when you use field(init=False) with an attribute in a dataclass, it means the attribute will not be included in the automatically generated __init__ method. This makes the attribute a non-initializable field, so you must set its value somewhere else in your class.

Typically, this is done in the __post_init__ method, which is automatically called after the dataclass's __init__ method.
"""
@dataclass
class Config:
    debug: bool = False
    app_name: str = "MyApp"
    version: str = field(init=False)

    def __post_init__(self):
        self.version = "1.0.0"

config = Config()
print(config)  # Output: Config(debug=False, app_name='MyApp')
print(config.version)  # Output: 1.0.0


"""
When to Use init=False Without __post_init__?
    You might not need __post_init__ if:
        The value will always be set manually later (e.g., by a method or external logic).
        The field is only used for internal purposes and doesn’t need to be initialized at object creation.
"""
@dataclass
class Task:
    name: str
    is_completed: bool = False
    _id: int = field(init=False)  # Internal field

    def generate_id(self):
        self._id = hash(self.name)

task = Task(name="Write Code")
task.generate_id()  # Set '_id' manually
print(task._id)  # Outputs a hash value




# Example 1: Storing Employee Data
@dataclass(order=True)
class Employee:
    id: int
    name: str
    age: int
    department: str
    salary: float = field(init=False, repr=False, compare=False) # Internal field

    def __post_init__(self):
        self.salary = 0

    def give_raise(self, amount):
        self.salary += amount

e1 = Employee(1, "Ahmed", 20, "HR")
e2 = Employee(2, "Ahmed", 10, "HR")
e1.give_raise(5000)
print(e1.salary)  # Output: 5000.0
print(e1 > e2)  # False ,  The id field is used for comparison because it is the first field (and not marked with compare=False). Comparisons follow the order of fields defined in the dataclass. If you exclude the id field from comparisons using field(compare=False), then the next field (name) would be used for comparison. then the comparison will be like that 'Ahmed' > 'Ali'
print(e1 == e2) #False,  Equality is determined by comparing the values of all fields in the order they are defined in the class except attributes that are excluded from comparisons with "compare=False"



# Example 2: Nested Data Classes
# You can use one data class inside another.
@dataclass
class Address:
    city: str
    state: str
    zip_code: str

@dataclass
class Person:
    name: str
    age: int
    address: Address

addr = Address("Cairo", "EG", "12345")
p = Person("Ahmed", 30, addr)

print(p)  # Output: Person(name='Ahmed', age=30, address=Address(city='Cairo', state='EG', zip_code='12345'))


# Example 3: Equality Comparisons for Custom Objects
@dataclass
class Item:
    name: str
    price: float
    quantity: int

    def total_cost(self) -> float:
        return self.price * self.quantity

i1 = Item("Apple", 1.5, 10)
i2 = Item("Apple", 1.5, 10)

print(i1 == i2)  # Output: True (since all attributes of i1 and i2 are equal (name, price, quantity), i1 == i2 evaluates to True.)
# The == operator does not require order=True. The behavior of == in your example is based on the equality comparison (eq), not ordering.
print(i1.total_cost())  # Output: 15.0



# Example 4: Combining with @property for Custom Behavior
# You can still use @property to add dynamic attributes.
@dataclass
class Person:
    name: str
    age: int

    @property
    def is_adult(self) -> bool:
        return self.age >= 18
    

p = Person("Ahmed", 30)
print(p.is_adult)  # Output: True
# @property Decorator: Makes a method behave like an attribute. This means you can access is_adult without parentheses (()).



"""
Do I Have to Define a Data Type for Every Attribute or Method?
    Yes, in Python, when using data classes (and in general for type hints), it’s good practice to define data types (annotations) for attributes and method arguments/return values.

    What is an Annotation?
        Annotations in Python are hints about what types of values a variable, argument, or return value should have. These don’t enforce the type but help:
            Improve code readability.
            Enable static type checking with tools like mypy.
            Provide better editor/IDE support.


"""

# Example 5: Inventory Management
@dataclass
class Product:
    name: str
    price: float
    quantity: int

    @property
    def in_stock(self):
        return self.quantity > 0
    
    def sell(self, amount):
        if amount > self.quantity:
            raise ValueError(f"Not enough {self.name} in stock.")
        self.quantity -= amount

product = Product("Widget", 19.99, 10)
print(product.in_stock) # Output: True
product.sell(5)
print(product.quantity)  # Output: 5


# Example 2: Validating Inputs
# You can validate inputs using __post_init__:
@dataclass
class Temperature:
    celsius: float

    def __post_init__(self):
        if self.celsius < -273.15:
            raise ValueError("Temperature below absolute zero is not possible!")

# t = Temperature(-300)  # Raises ValueError and stops the code
try:
    t = Temperature(-300)
except ValueError as e:
    print(str(e))  # Output: Temperature below absolute zero is not possible!
