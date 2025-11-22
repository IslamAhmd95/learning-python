"""
A Mixin is a class designed to provide additional functionality to other classes through inheritance, but it is not intended to be instantiated on its own. Mixins are used to extend the behavior of classes without forming a rigid parent-child relationship.

Why Use Mixins?
    Code Reusability: Share common functionality across different classes.
    Separation of Concerns: Keep specific features in separate, modular classes.
    Composability: Add multiple behaviors to a class by inheriting multiple mixins.
    Avoiding Deep Hierarchies: Mixins allow adding features without deeply nesting inheritance.
"""
import json
from datetime import datetime

# Example: Logging Functionality
# A mixin can add logging to any class.
class LogginMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class Order(LogginMixin):
    def processingOrder(self, order_id):
        self.log(f"Order {order_id} has been processed")

order = Order()
order.processingOrder(123)  # Output: [LOG]: Order 123 has been processed


# Example: Adding Serialization
# A mixin for converting objects to JSON format.
class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)
    

class User(JsonMixin):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

user = User("Alice", "Alice@gmail.com", "password")
print(user.to_json())  # Output: {"name": "Alice", "email": "Alice@gmail.com", "password": "password"}



# Example: Timestamp Logging
# A mixin for adding timestamps to logs.
class TimestampMixin:
    def log_with_timestamp(self, message):
        print(f"{datetime.now()}: {message}")

class EventLogger(TimestampMixin):
    def log_event(self, event_name):
        self.log_with_timestamp(f"Event: {event_name}")

# Example usage:
logger = EventLogger()
logger.log_event("System Boot")  # Output: 2025-01-08 19:33:47.485191: Event: System Boot


# Example:  Role-Based Access Control
# A mixin for handling permissions.
class RoleMixin:
    def has_permission(self, role):
        return role in self.roles

class Dashboard(RoleMixin):
    def __init__(self):
        self.roles = ["admin", "editor"]


dashboard = Dashboard()
print(dashboard.has_permission("admin"))  # True
print(dashboard.has_permission("user"))   # False



# Example: Default String Representation
# A mixin for providing a default __str__ implementation.
class StringMixin:
    def __str__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

class User(StringMixin):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


user = User("Alice", "alice@gmail.com", "password")
print(user)  # Output: User({'name': 'Alice', 'email': 'alice@gmail.com', 'password': 'password'})



# Example: Validation
# A mixin for validating inputs.
class ValidationMixin:
    def validate_age(self, age):
        if age < 0:
            raise ValueError("Age must be non-negative")
        return age
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
        
class User(ValidationMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = self.validate_age(age)


try:
    user = User("Alice", -10)
    # user = User("Alice", 10)
    print(user)  # Output: User({'name': 'Alice', 'age': 10})
except ValueError as e:
    print(e)  # Output: Age must be non-negative



# Example: Multiple Behaviors Using Mixins
# Combining mixins for different behaviors.
class FlyMixin:
    def fly(self):
        print("Flying high!")

class SwimMixin:
    def swim(self):
        print("Swimming fast!")

class Bird(FlyMixin, SwimMixin):
    def sound(self):
        print("Chirp chirp!")

# Example usage:
bird = Bird()
bird.fly()  # Flying high!
bird.swim()  # Swimming fast!
bird.sound()  # Chirp chirp!


# Example: Caching Mechanism
# A mixin for caching results of a method.
class CacheMixin:
    _cache = {}

    def cache_result(self, key, value):
        self._cache[key] = value

    def get_cached(self, key):
        return self._cache.get(key)

class WeatherService(CacheMixin):
    def fetch_weather(self, city):
        if (cached := self.get_cached(city)) is not None:
            return f"Cached weather for {city}: {cached}"
        # Simulate fetching weather
        weather = f"{city}: Sunny 25°C"
        self.cache_result(city, weather)
        return weather

# Example usage:
service = WeatherService()
print(service.fetch_weather("Cairo"))  # Cairo: Sunny 25°C
print(service.fetch_weather("Cairo"))  # Cached weather for Cairo: Cairo: Sunny 25°C
"""
Understanding the Walrus Operator ':='
    The walrus operator (assignment expression) allows you to assign a value to a variable as part of an expression. It's particularly useful for cases where you need to:

        Assign a value.
        Use that value in a condition or other expression.
            How it Works in the Code

            if (cached := self.get_cached(city)) is not None:
            This line does the following:

                Calls self.get_cached(city) to check if the city's weather is already cached.
                Assigns the result to the variable cached.
                Checks if cached is not None:
                    If cached contains a value, the if block executes and returns the cached data.
                    If cached is None, the program moves to the next line to "fetch" the weather.
                This avoids calling get_cached twice (once for checking and again for retrieval).
"""


"""
Best Practices with Mixins
    Descriptive Names: Use Mixin in the class name for clarity (e.g., LoggingMixin).
    Single Responsibility: Each mixin should focus on one functionality.
    Avoid Conflicts: Ensure mixins do not have overlapping methods or attributes.
    Use Sparingly: Too many mixins can lead to complex inheritance hierarchies.
"""