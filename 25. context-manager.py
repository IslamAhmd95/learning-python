from contextlib import contextmanager
import threading


"""
A context manager in Python is a function or a class that allows you to manage resources efficiently. It ensures that specific actions are performed before and after a block of code, such as opening and closing files, acquiring and releasing locks, or opening and closing database connections. It does this using the with statement, which provides a clear and concise way to manage resources and ensure they are properly cleaned up, even if an exception occurs.

The with statement simplifies resource management by automatically handling setup and cleanup tasks, such as opening/closing files or acquiring/releasing locks. You define a context manager by implementing two essential methods:

    __enter__(): This method defines the setup actions. It is executed when the with block is entered.
    __exit__(): This method defines the cleanup actions. It is executed when the with block is exited, whether normally or due to an exception.

    
# Using the open() function as a context manager
    with open("example.txt", "w") as file:
        file.write("Hello, world!")
    # File is automatically closed after the with block
In this case:
    The open() function acts as a context manager. It handles opening the file and automatically closing it after the block is executed.
    __enter__(): The file is opened.
    __exit__(): The file is automatically closed after exiting the block.


Why Use a Context Manager?
    Automatic Resource Management:
        Context managers ensure that resources are properly cleaned up, regardless of whether an error occurs. This helps avoid resource leaks (e.g., not closing files).
    Simplifies Code:
        The with statement makes code cleaner and more readable, reducing boilerplate code.
    Error Handling:
        Context managers ensure that cleanup is done, even if exceptions are raised within the with block.

Returning True in __exit__:
    Returning True suppresses exceptions raised inside the with block, allowing the program to continue execution.
    If you want the exception to propagate and stop the program, return False or remove the return statement.
"""

class DatabaseConnection:

    def __enter__(self):
        print("Connect to database")
        # Simulating opening a database connection
        self.connection = "Connecting ..."
        return self.connection  # This value is returned to the `with` block

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Disconnect from database")
        # Simulating closing the database connection
        self.connection = "Disconnecting ..."
        if exc_type:
            print(f"An error occurred: exc_type: {exc_type}, exc_value: {exc_val}, exc_traceback: {exc_tb}")
        
        return True  # Prevent the exception from propagating if desired
    
# Using the custom context manager
with DatabaseConnection() as connection:   # don't forget the parentheses in the class
    print(f"Using:{connection}")
    # Simulating some work with the database
    # If you raise an exception here, __exit__ will still be called
    raise Exception("Some error")  # Uncomment to see the exception handling in action


print("After the with block")  # if there's some exception raised, this will execute if the exit block returns True, if False the program will crash 

"""
Explanation:
    __enter__() is called when entering the with block and it sets up the database connection.
    __exit__() is called when exiting the with block and it ensures the database connection is closed properly.
    If an exception occurs in the with block, __exit__() will still handle the cleanup.
"""

"""
output if no exception is raised:
    Connect to database
    Using:Connecting ...
    Disconnect from database

output if the exception is raised and exit method returns True:
    Connect to database
    Using:Connecting ...
    Disconnect from database
    An error occurred: exc_type: <class 'Exception'>, exc_value: Some error, exc_traceback: <traceback object at 0x7bc377b395c0>
    After the with block    # the program didn't crash and completed excution after the with block

output if the exception is raised and exit method returns False:
    Connect to database
    Using:Connecting ...
    Disconnect from database
    An error occurred: exc_type: <class 'Exception'>, exc_value: Some error, exc_traceback: <traceback object at 0x766d3c7395c0>
    Traceback (most recent call last):
    File "/home/islam/Downloads/Python/25. context-manager.py", line 52, in <module>
        raise Exception("Some error")  # Uncomment to see the exception handling in action
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Exception: Some error    # the program crashes and the print statement after with block did not execute

"""

#----------------------------------------------------------------

lock = threading.Lock()

class LockContextManager:
    def __enter__(self):
        lock.acquire()
        print("Lock acquired.")
        return lock

    def __exit__(self, exc_type, exc_val, exc_tb):
        lock.release()
        print("Lock released.")

with LockContextManager():
    # Critical section (thread-safe code)
    print("Performing work within the locked section.")

"""
Here, the LockContextManager acquires the lock on entering the with block and releases it on exiting the block.
"""

"""
output:
Lock acquired.
Performing work within the locked section.
Lock released.
"""

#----------------------------------------------------------------

"""
Creating a Context Manager Using contextlib
    You can also use the contextlib module to create context managers without defining a full class. It provides the contextmanager decorator to simplify the process.

The code before yield is executed when entering the with block (setup).
The code after yield is executed when exiting the with block (cleanup).
"""

@contextmanager
def open_resource():
    print("Opening resource.")
    yield "Resource"  # This is what will be returned to the `with` block
    print("Closing resource.")

with open_resource() as resource:  # resource is the returned value from yield statement
    print(resource)

"""
output:
Opening resource.
Using: Resource
Closing resource.
"""

#----------------------------------------------------------------

"""
A context manager is a class or function that manages resources with setup (__enter__()) and cleanup (__exit__()).
with statement makes it easier and cleaner to handle resources by automatically invoking __enter__() and __exit__().
It's best practice to use context managers to manage resources because they ensure proper cleanup (e.g., closing files, releasing locks), even if an error occurs during execution.
"""

#----------------------------------------------------------------

# Comparison of Class and Function Context Managers

# class as a context manager
class FileHandler:
    def __enter__(self):
        print("file is opening")
        self.file = open("test.txt", "w")  # change w to r to trigger the exception
        print('file is opened')
        return self.file

    #  The __exit__ method is specifically designed to handle any exceptions that occur within the with block. This makes using a separate try-except block inside the with statement unnecessary.
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("file is ready to be closed")
        self.file.close()
        print("file is closed")
        if exc_type:
            print(f"An error occurred: exc_type: {exc_type}, exc_value: {exc_val}, exc_traceback: {exc_tb}")
        return True  # in case of there's an exception, False to stop the program and True to continue execution after printing the error occurred message

with FileHandler() as file:
    print("start writing to file ...")
    file.write("class as a context manager")
    print("finish writing to file")


"""
How It Works Without try-except ?

    When you use the with FileHandler() as file: statement:
        The __enter__ method is called, opening the file and returning it.
        The code inside the with block is executed.
        
    If an exception occurs (e.g., file.write("hello world!") raises an exception because the file is in "r" mode):
        The __exit__ method is automatically invoked.
        The exception details (exc_type, exc_val, exc_tb) are passed to the __exit__ method.

    Inside __exit__:
        The file is properly closed.
        The exception is logged or handled as specified.
        The return True ensures that the exception is suppressed, allowing the program to continue execution.
"""
"""
output:
file is opening
file is opened
start writing to file ...
finish writing to file
file is ready to be closed
file is closed
"""


# function as a context manager
@contextmanager
def FileHandler(file_path, mode):
    print("file is opening")
    file = open(file_path, mode)
    print('file is opened')
    yield file
    print("file is ready to be closed")
    file.close()
    print("file is closed")

with FileHandler("test.txt", "w") as file:
    print("start writing to file ...")
    file.write("Function as a context manager")
    print("finish writing to file")

"""
output:
file is opening
file is opened
start writing to file ...
finish writing to file
file is ready to be closed
file is closed
"""

#----------------------------------------------------------------

"""
When a function is used as a context manager with the @contextmanager decorator from contextlib, it acts as a generator because it uses yield. This design ensures that:

    - Setup code (everything before the yield) is executed first when the with block is entered.
    - The function "pauses" at the yield, and control is passed to the with block, allowing the resource to be used.
    - Cleanup code (everything after the yield) is executed only when the with block is exited—whether it exits normally or due to an exception.

Why Use yield?
    yield allows the function to maintain its state across entry and exit points of the with block.
    It essentially splits the function into two phases:
        The setup phase (before yield).
        The cleanup phase (after yield).

Yield Makes the Function a Generator
    - When a function uses yield, it becomes a generator. This means it can produce values lazily, pausing execution at each yield and resuming from where it left off when next() is called.
    - By using @contextmanager, the generator is repurposed "يعاد استخدامه" to act as a context manager. - Instead of looping or calling next(), the with statement handles the lifecycle:
        It runs the code before yield when entering the with block.
        It runs the code after yield when exiting the with block.


It's Not a Generator Directly
    A plain generator function with yield produces a generator object that is iterable.
    However, the @contextmanager decorator adds additional behavior to manage setup and cleanup operations as part of the context manager protocol. This behavior makes it incompatible with being a plain generator.
    If your goal is to iterate over a generator, you should remove the @contextmanager decorator
"""

#----------------------------------------------------------------

"""
__enter__() Method
    Purpose: Defines the setup behavior for the resource.
    Parameters: It does not accept arguments (other than self).
    Return Value: It can return any object that you want to use in the with block.

__exit__() Method
    Purpose: Defines the cleanup behavior for the resource.
    Parameters:
        exc_type: The type of the exception (if any) raised in the with block.
        exc_value: The value of the exception (if any).
        traceback: The traceback object (if any).
    Return Value: If True is returned, it suppresses the exception raised in the with block. Otherwise, the exception propagates.
    The parameters allow your context manager to handle exceptions if they occur inside the with block.

What is exc_value?
    exc_value usually holds the message inside the exception or the exception object itself. For example:
        raise ValueError("This is an error message.")
        exc_type = "This is an error message."

What is exc_type?
    exc_type tells you the type of the exception that occurred.
    It’s the class of the exception (e.g., ValueError, TypeError, etc.). For example:
        try:
            raise ValueError("This is an error.")
        except ValueError as e:
            print(type(e))  # Output: <class 'ValueError'>

What is traceback?
    traceback shows the line of code and the path where the error happened.
    It’s like a "map" that helps you understand where and why the error occurred. For example:
        try:
            raise ValueError("This is an error.")
        except ValueError as e:
            import traceback
            traceback.print_exc()
        
        the output should be something like this:
            Traceback (most recent call last):
            File "<file_name>", line 2, in <module>
                raise ValueError("This is an error.")
            ValueError: This is an error.


What does "suppress the exception" mean?
        Normally, if an error occurs in Python, it stops your program and shows the error message.
        Suppressing "قمع" the exception means "ignoring" the error and continuing the program as if nothing happened.
    If __exit__() returns True, it suppresses (hides) the exception. If it returns False (or nothing), the error is still raised, and the program stops unless handled.


What does "exception propagates 'ينشر' " mean?
    "Exception propagates" means the error is not suppressed. Instead, the error continues to be raised, and the program will stop unless you handle the error outside the with block.
"""