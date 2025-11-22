"""
A docstring is a special type of string used to document a specific segment of code, such as a function, class, or module. Docstrings provide a convenient way to include documentation directly within the code.

Docstrings are written as the first statement in a function, class, or module, enclosed in triple quotes (""" """ or ''' ''').
"""

def add(a, b):
    """
    Add two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
    """
    return a + b


class BankAccount:
    """
    A simple class representing a bank account.

    Attributes:
    name (str): The name of the account holder.
    balance (float): The account balance.
    """

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


# Docstrings can be accessed using the __doc__ attribute of the documented object.
print(add.__doc__)
print(BankAccount.__doc__)


#----------------------------------------------------------------

# The Python help() function is a built-in utility that displays the documentation (including docstrings) of a module, class, method, or function in a user-friendly way. It extracts and formats the docstring of the object you pass to it.

# print(help(add))
# print(help(BankAccount))



"""
1- __doc__ is a simple and direct way to access docstrings as raw text.
2- help() is a powerful tool for providing detailed and formatted information, ideal for interactive use and exploration.
"""
