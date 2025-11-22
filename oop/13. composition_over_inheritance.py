"""
Composition over Inheritance is a principle in object-oriented design that promotes using object composition (combining simple objects to build complex ones) instead of inheritance (deriving classes from other classes). This approach is often more flexible, maintainable, and reusable.

The core idea behind Composition Over Inheritance. Instead of defining a feature in a parent class and risking that some subclasses may not need it (or may need a different variation of it), you encapsulate each feature in its own class and then include that class in any object that needs the feature.

Why Composition Over Inheritance?
    Avoiding the Fragile Base Class Problem:
        Inheritance tightly couples child classes to their parent classes. Changes in the base class can inadvertently affect all derived classes.
        Composition, on the other hand, involves creating classes with loosely coupled objects. This makes the design more resilient to change.
        
    Better Code Reusability:
        With composition, you can combine behaviors from multiple objects rather than being restricted to inheriting from a single base class.

    More Flexible Relationships:
        Composition allows "has-a" relationships instead of the strict "is-a" relationship of inheritance. For example, "A Car has an Engine" vs. "A Car is a Vehicle."

    Supports Dynamic Behavior:
        Composition allows for runtime behavior changes by swapping out or modifying components.

        
When to Use Composition Over Inheritance
    When Relationships Are Unclear:
        If "is-a" doesn't clearly define the relationship, use composition.

    For Reusability:
        If you anticipate reusing components independently of a hierarchy, composition is better.

    For Scalability:
        As systems grow, composition reduces the risk of overly complex hierarchies.

    When Flexibility Is Needed:
        Use composition if different objects need to have interchangeable behaviors.


Why This Approach Works Well
    Avoids Unnecessary Features in Subclasses:
        In inheritance, if a feature is added to a parent class, all subclasses inherit it, even if it doesn’t make sense for them to have it.
        With composition, you only include the feature where it's actually needed.
        
    Encourages Single Responsibility:
        By separating features into their own classes, each class has a single, well-defined responsibility, making the code easier to understand and maintain.

    Promotes Flexibility:
        Different classes can "compose" themselves differently by including only the features they need.

        
When to Use Inheritance
    While composition is powerful, inheritance is still useful when:
        You have a clear "is-a" relationship (e.g., Cat is a type of Animal).
        The behavior is shared across all subclasses and is unlikely to change (e.g., Animal.eat()).
"""

# Example 1: Vehicle and Engine

# Problem with Inheritance:
class Vehicle:
    def start(self):
        print("Starting vehicle...")
        
class Car(Vehicle):
    pass

class Boat(Vehicle):
    pass

# If you add a new feature (e.g., fly for airplanes), you may end up with irrelevant methods in unrelated classes.

# Solution with composition
class Engine:
    def start(self):
        print("starting engine...")

class Vehicle:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

class Car(Vehicle):
    pass

class Boat(Vehicle):
    pass

engine = Engine()
car = Car(engine)
boat = Boat(engine)

car.start()  # Output: starting engine...
boat.start()  # Output: starting engine...



# Example 2: Notification System

# Problem with Inheritance:
class EmailNotification:
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotification(EmailNotification):  # Doesn't make sense as Email is unrelated to SMS
    def send(self, message):
        print(f"Sending SMS: {message}")


# Solution with composition:
class EmailNotification:
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotification:  
    def send(self, message):
        print(f"Sending SMS: {message}")

class Notifications:
    def __init__(self, notification_types):
        self.notification_types = notification_types

    def send_notifications(self, message):
        for notification_type in self.notification_types:
            notification_type.send(message)


email_notification = EmailNotification()
sms_notification = SMSNotification()

notifications = Notifications([email_notification, sms_notification])
notifications.send_notifications("Hello!")
# Output:
# Sending email: Hello!
# Sending SMS: Hello!


# Example 3: Game Characters

# Problem with Inheritance:
    # A Character class with subclasses Warrior, Mage, Archer might result in too many subclasses for combinations like MageWarrior.

# Solution with composition:
class Weapon:
    def use(self):
        pass

class Sword(Weapon):
    def use(self):
        print("Swinging sword!")

class Bow(Weapon):
    def use(self):
        print("Shooting arrow!")

class Character:
    def __init__(self, weapon):
        self.weapon = weapon

    def attack(self):
        self.weapon.use()

# Usage
sword = Sword()
bow = Bow()

warrior = Character(sword)
archer = Character(bow)

warrior.attack()  # Output: Swinging sword!
archer.attack()   # Output: Shooting arrow!



# Example4: designing a system for Animals.

# Problem with Inheritance:
class Animal:
    def eat(self):
        print("Eating food")

    def fly(self):
        print("Flying")  # Not all animals can fly

class Bird(Animal):
    pass

class Dog(Animal):
    pass

bird = Bird()
dog = Dog()

bird.fly()  # Output: Flying
dog.fly()   # Output: Flying,  Doesn't make sense for a dog to fly

# Here, the fly method is unnecessary for Dog, but it exists because it’s defined in the parent Animal class.


# Solution with Composition:
class FlyBehavior:
    def fly(self):
        print("Flying...")

class Animal:
    def __init__(self, fly_behavior = None):
        self.fly_behavior = fly_behavior

    def fly(self):
        if self.fly_behavior is not None:
            return self.fly_behavior.fly()
        print("Can't fly")

    def eat(self):
        print("Eating food...")

class Dog(Animal):
    pass

class Bird(Animal):
    pass

fly_behavior = FlyBehavior()

for animal in [Bird(fly_behavior), Dog()]:
    animal.eat()
    animal.fly()

"""
Output:
Eating food...
Flying...
Eating food...
Can't fly

Explanation:
Feature as a Separate Class: FlyBehavior encapsulates the flying feature. If other animals need the ability to fly, you simply reuse this class.

Flexible Behavior: The fly method in Animal delegates the flying behavior to FlyBehavior if it exists. If not, it handles the absence of the feature gracefully.

No Unwanted Features: The Dog object doesn’t have the FlyBehavior, so it doesn’t inherit the fly method unnecessarily.
"""

