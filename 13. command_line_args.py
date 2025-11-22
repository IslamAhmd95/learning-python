## Using Sys.argv

# sys.argv is a list in Python that contains the command-line arguments passed to the script.
# The first element, sys.argv[0], is the name of the script itself.
# Subsequent elements (sys.argv[1], sys.argv[2], etc.) are the arguments passed to the script.

# import sys

# Example:

# print(sys.argv)  # ['13. command_line_args.py', '1', '2']
# print(len(sys.argv))  # 3
# print(sys.argv[0])  # 13. command_line_args.py
# print(sys.argv[0:])  # ['13. command_line_args.py', '1', '2']

# # run python3 13.\ command_line_args.py 1 2 on the command line
# # \ is a scape character used in the command line to scape the space

# if len(sys.argv) < 3:
#     sys.exit("Usage: python script.py num1 num2 ..")

# try:
#     numbers = list(map(int, sys.argv[1:]))
#     print(f"Sum of numbers is {sum(numbers)}")
# except ValueError:
#     exit("Both arguments must be integers")


#----------------------------------------------------------------


## Using argparse

import argparse 

# Components of argparse
# ArgumentParser: The main entry point to create an argument parser.
# add_argument: Used to define the arguments your script accepts.
# parse_args: Parses the command-line arguments and returns them as an object.

# Example:

# parser = argparse.ArgumentParser(description="Program to add 2 numbers")
# parser.add_argument("num1", type=int, help="first number")
# parser.add_argument("num2", type=int, help="second number")

# args = parser.parse_args()
# print(args)  # Namespace(num1=1, num2=2)
# print(type(args)) # <class 'argparse.Namespace'>
# print(f"\nThe sum of the numbers is {args.num1 + args.num2}")


# Example:

# Explanation of Methods
# 1. ArgumentParser
# Creates a parser object to handle arguments.
# description: Provides a brief description of your program.
# Example:
parser = argparse.ArgumentParser(description="Calculator program")

# 2. add_argument
# Used to define the arguments your script accepts.
# Example:
parser.add_argument("num1", type=int, metavar="First Number", help="first number")
parser.add_argument("num2", type=int, metavar="Second Number", help="second number")

parser.add_argument("-o", "--operation", type=str, choices=["add", "subtract", "multiply", "divide"], default="add", help="The operation to perform. Choices: add, subtract, multiply, divide (default: add)")

# 3. parse_args
# Parses the command-line arguments and returns them as an object.
# Example:
args = parser.parse_args()
print(args.num1)  # Access the num1 argument
print(args.operation)  # Access the operation argument

# Run the file with python3 calculator.py 10 5 -o add | python calculator.py 10 5 --operation add
# When you run python3 13.\ command_line_args.py --help , argparse automatically generates usage instructions

#output:

    # A simple calculator.

    # positional arguments:
    # First Number          first number
    # Second Number         second number

    # optional arguments:
    # -h, --help            show this help message and exit
    # -o {add,subtract,multiply,divide}, --operation {add,subtract,multiply,divide}
    #                         The operation to perform. Choices: add, subtract, multiply, divide (default: add)


# Key Points :
# argparse makes scripts user-friendly with help messages and error handling.
# Use positional arguments (num1, num2) for required inputs and optional arguments (operation) for flexibility.
# Use choices to restrict values for an argument.
# Default values prevent missing argument errors.
# Test your script with --help to ensure it is intuitive.
# The required attribute is used with optional arguments (arguments that use - or --) to make them mandatory. By default, optional arguments are not required.
# The metavar attribute changes how arguments are displayed in the help message. It is particularly useful for improving the readability of usage instructions.



# Key Differences Between Positional and Optional Arguments:

"""
Positional Arguments:

These arguments are identified by their position in the command-line input, not by a flag (e.g., numbers in your code), and can't use required attribute with them .
Positional arguments are required by default in argparse unless a default value is provided or nargs='?' is used.

example:
parser.add_argument("numbers", type=int, nargs='+', metavar="numbers", help="numbers to operate")

numbers is positional because it does not have a prefix like - or --.
The nargs='+' means one or more values are expected for this argument. Since at least one value must be provided, it is inherently required.
"""
"""
Optional Arguments:

These are identified by flags, e.g., -o or --operation.
They are optional by default unless explicitly marked as required with required=True.

example:
parser.add_argument("-o", "--operation", type=str, choices=["add", "subtract", "multiply", "divide"], default="add", help="The operation to perform.")

-o is optional because it has a default value (default="add") and does not require explicit input.
"""



"""
The nargs parameter in Python's argparse module specifies how many arguments a command-line argument can take. It works for both positional and optional arguments.
nargs='*' means 0 or more values are expected for this argument.
nargs='+' means one or more values are expected for this argument
nargs='?' means 0 or 1 value is expected for this argument.
nargs=n  means specific values n are expected for this argument

nargs=argparse.REMAINDER  Collects all remaining arguments, regardless of their format.
example:
python script.py run --verbose --debug
output: ['run', '--verbose', '--debug']
"""