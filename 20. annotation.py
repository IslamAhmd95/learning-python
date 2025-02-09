"""
Annotations in Python provide a way to associate metadata with variables, function arguments, and return values. They are typically used for type hints but can also store any other kind of information.

Annotations don’t affect the runtime behavior of the program—they are purely informational. However, tools like type checkers (mypy) and IDEs can use them for static type checking and improved code suggestions.
"""

#----------------------------------------------------------------

"""
1. Function Annotations
Annotations for function parameters and return values are specified using a colon : and an arrow ->.

def function_name(param1: type, param2: type) -> return_type:
    pass
"""

def greet(name: str) -> str:
    return f"Hello, {name}"

print(greet.__annotations__)

#----------------------------------------------------------------

"""
2. Variable Annotations
Variables can also have annotations, but they are optional.

variable_name: type = value
"""

age: int = 25
name: str = "John"
pi: float = 3.14

#----------------------------------------------------------------

"""
3. Accessing Annotations

Annotations for functions are stored in a dictionary called __annotations__.

print(greet.__annotations__)  # {'name': <class'str'>, 'return': <class'str'>}


the __annotations__ attribute is available for functions, classes, and modules to store type hints. However, it is not available for variables defined at a function level. It is only accessible for module-level variables (global scope) or class-level attributes.

Annotations for variables inside the function (e.g., z: float) are not stored in __annotations__, as __annotations__ is reserved for function-level annotations (parameters and return type).

def example():
    z: float = 3.14
    return "Hello"

print(example.__annotations__)  # Output: {}


"""

def add(a: int, b: int) -> int:
    return a + b

print(add.__annotations__)
# Output: {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}

#----------------------------------------------------------------

"""
4. Benefits of Annotations
Improved Readability: Indicate the intended use and types.
Static Type Checking: Tools like mypy check type consistency.
Documentation: Act as lightweight documentation for functions and variables.
"""

#----------------------------------------------------------------

"""
5. Optional Use Cases
Annotations are not enforced at runtime. For example, the following code will work even if the types don’t match and will not produce errors.
Python annotations are not enforced: They're just hints.
You can pass or assign any type, even if it doesn't match the annotation.
"""

def multiply(x: int, y: int) -> int:
    return x * y

print(multiply("Hello", 3))  # Output: HelloHelloHello

#----------------------------------------------------------------

"""
6. Using typing Module
Python's typing module provides advanced type hints:

List, Tuple, Dict
Union
Optional
Callable
"""

from typing import List, Optional

def find_item(items: List[str], key: str) -> Optional[str]:
    return key if key in items else None

print(__annotations__)  # print modules variables annotations