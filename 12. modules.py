from math import pi
import sys as s  # we can use as with import 
import random as rdm # rdm is aliase, we have to use it not the module name
from enum import Enum
from my_modules import kansas
# from my_modules.kansas import welcome, state
# If you want my_modules to be treated as a package, adding an __init__.py is a clear indicator. While Python 3.3+ automatically considers directories with Python files as packages, the presence of __init__.py makes it explicit.

print(type(s))  # <class 'module'>
print(kansas.state)  #prints kansas 
print(pi)  # 3.14
print(rdm.choice("islam"))  # random character

# print(dir(rdm)) # The dir() function in Python is a built-in utility that returns a list of attributes and methods associated with an object (rdm).
x = 5
y = 4
# print(dir())  # dir() without arguments lists all variables, functions, or imported modules in the current scope. In this case, it shows x, y, and other built-ins.

# 1. What is __name__?
# __name__ is a special built-in variable in Python.
# It stores the name of the module currently being executed.
# 2. What is __main__?
# If a Python file is executed directly, the value of __name__ is set to "__main__".
# If a file is imported as a module, the value of __name__ is the name of the module (e.g., kansas).

if __name__ == "__main__":
    print("modules file is currently executing, and kansas is an imported module")

print(__name__)  # __main__
print(kansas.__name__)  # my_modules.kansas


import platform

print(type(platform))  # <class 'module'>
x = platform.system()
print(x)  # Linux
print(type(x)) # <class 'str'>
print(dir(x))