"""
A generator is a special type of iterator in Python. It simplifies the creation of iterators using a function instead of a class.

Generators are defined like regular functions but use the yield keyword to produce values one at a time.
They automatically maintain their state between calls, making them memory-efficient for large sequences.

yield vs return
    return terminates the function and returns a value.
    yield pauses the function, saves its state, and returns a value. When the generator is resumed, it continues execution from where it left off.

Generators as Iterators
    Generators automatically implement the __iter__() and __next__() methods, making them iterators. You can use them in a for loop or call next() on them.
"""

# Example:
def produceNumber():
    yield 1
    yield 2
    yield 3


# Create a generator object
generator = produceNumber()
for num in generator:
    print(num)  # 1 2 3


# Example:
def countdown(n):
    # for i in range(n, 0, -1):
    #     yield i

    while n > 0:
        yield n
        n -= 1  # decrement the counter by 1 before yielding the value


for x in countdown(5):
    print(x)  # 5 4 3 2 1


# Example:
def evenNumbers(n):
    for i in range(0, n, 2):
        yield i

    # raise StopIteration("No more even numbers to generate") # the StopIteration exception does not carry a default error message unless explicitly "ضمنيا" provided by the generator.


for x in evenNumbers(11):
    print(x)  # 0 2 4 6 8 10

evenNumbersObj = evenNumbers(11)
print(next(evenNumbersObj))  # 0
print(next(evenNumbersObj))  # 2
print(next(evenNumbersObj))  # 4
print(next(evenNumbersObj))  # 6
print(next(evenNumbersObj))  # 8
print(next(evenNumbersObj))  # 10
# print(next(evenNumbersObj))  # StopIteration error 

# practice try-except also with generators
evenNumbersObj2 = evenNumbers(13)
try:
    for i in range(0, 15):
        print(next(evenNumbersObj2))
except StopIteration as error:  # it will use the upper commented raise stopiteration exception
    print(f" Iteration stopped due to {error}")

#----------------------------------------------------------------

"""
Why Use Generators?
Generators are useful when you don’t want to store the entire sequence in memory.
"""

def fibonacci(n):  # The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers.
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(15):
    print(num)  # 0 1 1 2 3 5 8 13 ... 377

"""
Explanation

Start with a = 0 and b = 1.
On the first iteration, yield a returns 0.
Then, a, b = b, a + b sets:

a = 1 (the old value of b)
b = 1 (a + b, where a was 0 and b was 1).
On the second iteration, yield a returns 1.
Then, a, b = b, a + b updates:

a = 1 (the old value of b)
b = 2 (a + b, where a was 1 and b was 1).
On the third iteration, yield a returns 1.
Then, a, b = b, a + b updates:

a = 2 (the old value of b)
b = 3 (a + b, where a was 1 and b was 2).
On the fourth iteration, yield a returns 2.
Then, a, b = b, a + b updates:

a = 3 (the old value of b)
b = 5 (a + b, where a was 2 and b was 3).
On the fifth iteration, yield a returns 3.
Then, a, b = b, a + b updates:

a = 5 (the old value of b)
b = 8 (a + b, where a was 3 and b was 5).
The loop ends after 5 iterations (n = 5), so the generator stops

a gets the old value of b.
b gets the sum of the old values of a and b.
"""
#----------------------------------------------------------------

"""
Generator Expressions
    Generator expressions provide a compact way to create generators, similar to list comprehensions but with parentheses instead of brackets.
"""

gen = (x*x for x in range(1, 5))
print(gen) # <generator object <genexpr> at 0x7fdd76b13ac0>
print(type(gen))  # <class 'generator'>
print(next(gen)) # 1
print(next(gen)) # 4
print(next(gen)) # 9
print(next(gen)) # 16
# print(next(gen)) # raise stopiteration error

#----------------------------------------------------------------

"""
Iterable
    Any object that can be looped over
    Lists, tuples, dictionaries
    No state management
    Higher memory usage (stores all items)

Iterators
    Tool to fetch values one by one
    Object with __iter__ and __next__
    Maintains state between calls
    Lower memory usage (fetches one item at a time)

Generators
    Simplified way to create iterators
    Function with yield
    Maintains state between calls
    Lower memory usage (fetches one item at a time)
"""

#----------------------------------------------------------------

"""
1. Does yield work like next()?
    - yield pauses the function and sends the current value back to the caller. When the generator is resumed (e.g., by calling next() or using a for loop), execution continues from where it was paused.
    - next() is used to get the next value from an iterator or generator.

So while they are related, they are not the same:
    - yield is used inside a generator function to produce values one at a time.
    - next() is used outside a generator or iterator to retrieve the next value.


def my_gen():
    yield 1
    yield 2
    yield 3

gen = my_gen()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
Here, yield defines what value to produce, and next() retrieves that value.


1. Does yield work like next()?
    yield pauses the function and sends the current value back to the caller. When the generator is resumed (e.g., by calling next() or using a for loop), execution continues from where it was paused.
    next() is used to explicitly get the next value from an iterator or generator.

So while they are related, they are not the same:
    yield is used inside a generator function to produce values one at a time.
    next() is used outside a generator or iterator to retrieve the next value.

For example:

    def my_gen():
        yield 1
        yield 2
        yield 3

    gen = my_gen()

    print(next(gen))  # Output: 1
    print(next(gen))  # Output: 2
    print(next(gen))  # Output: 3
    Here, yield defines what value to produce, and next() retrieves that value.

2. Does yield return the result that will be printed inside the for loop?
Yes, exactly! When a for loop is used with a generator, it implicitly calls next() on the generator to retrieve the values. The yield keyword determines what is returned at each step, and that is what gets printed or processed in the loop.

For example:

    def count_up_to(n):
        for i in range(1, n + 1):
            yield i

    for num in count_up_to(3):
        print(num)

    This is equivalent to:

    gen = count_up_to(3)

    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3
    In both cases, the values produced by yield (1, 2, 3) are printed.


Why is yield Powerful?
    Using yield allows you to:
        Produce values lazily: Generate items one at a time, which is memory-efficient for large sequences.
        Pause and resume execution: The function's state (local variables) is maintained between calls.
"""

#----------------------------------------------------------------

"""
The "yield from" statement in Python is used to delegate "pass" part of the generator’s responsibility to another generator. When you use yield from, it allows one generator to yield all the values from another generator, instead of having to manually loop through and yield values one by one.

Why Does This Work?
    yield from works with any object that is iterable, meaning it can be looped over.
    Internally, when you use yield from iterable, Python:
        Calls iter(iterable) to get an iterator for the iterable.
        Iterates through the iterator using next() and yields each value.
        Stops when a StopIteration exception is raised by the iterator.
"""

def generator_one():
    yield 1
    yield 2

def generator_two():
    yield from generator_one()  # instead of looping through generator_one, yield from can do the job
    yield 3
    yield 4

for num in generator_two():
    print(f"{num} from generators")

# output
# 1 from generators
# 2 from generators
# 3 from generators
# 4 from generators

"""
generator_one():
    This is a simple generator function that yields two values: 1 and 2.
    The yield statement produces a value and pauses the function, allowing the value to be returned to the caller.

generator_two():
    This generator uses yield from generator_one(). What this does is delegate the responsibility of yielding values to generator_one().
    yield from automatically consumes all the values yielded by generator_one() and yields them one by one, without the need for a loop in generator_two.
    After generator_one() is exhausted (it yields 1 and 2), generator_two() continues to yield its own value, which is 3.

for value in generator_two()::
    The for loop iterates over generator_two(). Inside generator_two(), the first two values (1 and 2) are yielded from generator_one(), and then the final value (3) is yielded directly from generator_two().


What does yield from do?
    Delegation: yield from is a way to delegate part of the yielding process to another generator (or iterable). This allows the outer generator (generator_two()) to simply "pass on" the yielding responsibility to another generator (generator_one()).

    Simplification: Instead of manually iterating over generator_one() and yielding its values one by one, yield from handles that automatically.

    Efficiency: Using yield from is more efficient and concise compared to writing a loop to iterate over the sub-generator and yield each value manually.
"""

# This is functionally identical to the version with yield from, but it's more verbose.
def generator_two():
    for value in generator_one():
        yield value
    yield 3

"""
Key Points about yield from:
    Delegates to another generator: 
        yield from is used to delegate the yielding process to another iterable or generator.
    Automatically handles iteration: 
        It automatically loops through the other generator and yields values one by one.
    Simplifies generator code:
        Instead of manually yielding each value from a sub-generator, yield from makes the code more readable and concise.
    Works with any iterable:
        yield from works not only with generators but also with any iterable (e.g., lists, tuples).

        Example:

        def withList():
            yield from [1, 2, 3]  # Delegates to a list

        for value in withList():
            print(value)  1 2 3


            
        def withTuple():
            yield from (4, 5, 6)  # Delegates to a tuple

        for value in withTuple():
            print(value)  4 5 6


            
        def withString():
            yield from "Hello"  # Delegates to a string

        for char in withString():
            print(char)  H e l l o

"""

class CustomIterator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

def yieldFromClass(data):
    # yield from CustomIterator(data)
    yield from data  # I can yield directly from lists or any iterable object

for num in yieldFromClass([1, 2, 3, 4, 5]):
    print(f"yielding {num} from class")

# output
# yielding 1 from class
# yielding 2 from class
# yielding 3 from class
# yielding 4 from class
# yielding 5 from class

    
# ----------------------------------------------------------------

# More Examples

#Infinite Generator
#Generators can be used to create infinite sequences without memory issues.

def infiniteGen():
    num = 0
    while True:
        yield num
        num += 1

# for i in infiniteGen():  # this will last forever
#     print(i)

infiniteObj = infiniteGen()
print(next(infiniteObj))  # 0
print(next(infiniteObj))  # 1
print(next(infiniteObj))  # 2




# Simple Generator for Square Numbers
# A basic generator function that calculates squares of numbers lazily.

def squareGen(n):
    for i in range(n):
        yield i ** 2


for num in squareGen(3):
    print(num)  # 0 1 4


# Infine Generator for printing numbers
def printNumbers():
    num = 0
    while True:
        yield num
        num += 1

numbers = printNumbers()
for _ in range(5):
    print(next(numbers)) # 0 1 2 3 4





# filter even numbers and print them
def evenNumbers(start, end):
    current = start
    while current <= end:
        if current % 2 == 0:
            yield current
        current += 1

for num in evenNumbers(1, 6):
    print(num)  # 2 4 6




# Generator with Multiple Yields
# Yield multiple values step by step.
def step_by_step():
    print("First Step")
    yield 1
    print("Second Step")
    yield 2
    print("Third Step")
    yield 3


# The print statements are executed at each step, showing where the function is paused.
# Each yield returns a different message.
steps = step_by_step()
for step in steps:
    print(step)  # First Step, 1, Second Step, 2, Third Step, 3




# Combining Generators
# Chain multiple generators to process data in stages.

def numbers(n):
    for i in range(n):
        yield i

def squares(gen):
    for i in gen:
        yield i ** 2

def doubles(gen):
    for i in gen:
        yield i * 2

myNumbers = numbers(5)
squareNumbers = squares(myNumbers)
doubleNumbers = doubles(squareNumbers)

"""
integers() produces numbers: 1, 2, 3, 4.
squares() takes those numbers and squares them.
doubles() takes the squared numbers and doubles them.
The chain processes data step by step.
"""
for num in doubleNumbers:
    print(num)  # 0 2 8 18 32





# Stateful Generator
# Track cumulative sums of a sequence.
def cumulative_sum(list):
    total = 0
    for i in list:
        total += i
        yield total

numberslist = [1, 2, 3, 4, 5]
for cum_sum in cumulative_sum(numberslist):
    print(cum_sum)  # 1 3 6 10 15



def printIterable(iterable):
    yield from iterable

for i in printIterable([3]):
    for x in printIterable((1, 2, 3, 4)):
        print(i ** x)  # 3 9 27 81