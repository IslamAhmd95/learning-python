## Classes and Objects
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"This vehicle is a {self.make} {self.model}."
    
    def move(self):
        print("Moves along ..")


my_car = Vehicle("Tesla", "Model 3")
print(my_car.display_info())
my_car.move()

#----------------------------------------------------------------

## Inheritance

class Airplane(Vehicle):

    def __init__(self, make, model, faa_id):
        super().__init__(make, model)  # call the parent class constructor
        self.faa_id = faa_id

    def move(self): # overwrite the parent method move()
        print("Flies along ..")

class Truck(Vehicle):

    def move(self): # overwrite the parent method move()
        print("Rumbles along ..")

class GolfCart(Vehicle):
    pass  # The pass statement is a placeholder that does nothing, indicating that the class has no additional methods or attributes beyond what it inherits from Vehicle.

cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

print(cessna.display_info())
cessna.move()
print(mack.display_info())
mack.move()
print(golfwagon.display_info())
golfwagon.move()


#----------------------------------------------------------------


## Polymorphism 
# Polymorphism in programming refers to the ability of a function, method, or object to take on multiple forms. It allows the same interface or method to behave differently depending on the object calling it.

# such as animals making sounds or vehicles moving differently, i don't know or care about how but the action itself .

# you don't focus on the specific behavior of the object; instead, you focus on what the object is supposed to do (its interface or contract).

# Focus on the Action, Not the Details

# With polymorphism, you focus on the action or purpose (what you want the object to do) and trust that the object knows how to do it based on its type. This keeps your code clean, reusable, and extensible.

# Polymorphism makes it easy to add new behaviors or types without changing the existing code.

# For example, you could add a Boat class with its own move() method, and the loop would handle it automatically.
print('\n\n')
for v in [my_car, cessna, mack, golfwagon]:
    print(v.display_info())
    v.move()


# we can achieve polymorphism in 3 ways "method overriding, duck typing, and Polymorphism with Built-in Functions"

### 1- method overriding

class Animal:
    def make_sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def make_sound(self):   
        print("The dog barks.")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows.")

# The make_sound method is overridden in each subclass. When the loop iterates, it calls the appropriate method for each object dynamically.
for animal in [Dog(), Cat()]:
    animal.make_sound()


### 2- Duck typing

# Objects of different types can be used interchangeably if they implement the required behavior.

# This is known as duck typing, where the object's type is not explicitly checked or explicitly specified.

# How is Duck Typing Unique?

# No need to enforce inheritance:
# In many OOP languages, objects must share a common base class to be interchangeable.

# With duck typing, objects don’t have to inherit from a specific class. They only need to have the necessary methods or attributes.
# Focus on behavior, not type:

# In duck typing, if an object can do what you ask of it (like calling a method), you don't care about its type.

class Dog:

    def __init__(self, name):
        self.name = name

    def sound(self):
        return self.name + " has sound of Woof!"

class Cat:

    def __init__(self, name):
        self.name = name

    def sound(self):
        return self.name + " has sound of Meow!"

class Duck:

    def __init__(self, name):
        self.name = name

    def sound(self):
        return self.name + " has sound of Quack!"
    
def makes_sound(animal):
    print(animal.sound())

for animal in [Dog('Dog'), Cat('Cat'), Duck('Duck')]:
    makes_sound(animal)

# Explanation:

# Each object (Dog, Cat, Duck) is not related via inheritance or shared parent class.

# make_animal_sound doesn’t care about the type of the object (Dog, Cat, or Duck). It only calls the sound method.

# As long as the objects have the sound method, they can be used interchangeably.

# This is the core of duck typing: it behaves like a duck (has the sound method), so we treat it as one.


# Why Not Just Use Other Approaches?

# You might think this looks like polymorphism or other OOP techniques. Here’s how duck typing is different:

# 1- No inheritance or common parent class:
# In traditional polymorphism, objects often share a parent class or interface.
# In duck typing, they don't have to share anything. The only requirement is behavior.

# 2- Dynamic and Flexible:
# Duck typing relies on Python's dynamic nature. It allows you to pass objects of completely unrelated types as long as they implement the required methods.
# This is more flexible than explicitly enforcing inheritance.



### 3- Polymorphism with Built-in Functions
print(len("islam"))
print(len([1, 2, 3]))
print(len({"name": "islam", "age": 29}))

# Explanation: The len function is polymorphic. It knows how to calculate the length for different types of objects (strings, lists, dictionaries).




## Benefits of Polymorphism
# 1- Reduces code duplication.
# 2- Promotes flexibility in design.
# 3- Makes programs easier to maintain and extend.