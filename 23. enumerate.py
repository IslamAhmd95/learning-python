"""
The enumerate() function in Python is used to add a counter to an iterable (like a list, tuple, or string) and return it as an enumerate object. This is useful when you need both the index and the value of items while iterating.

Syntax:
    enumerate(iterable, start=0)
    iterable: Any iterable object (e.g., list, tuple, string, etc.).
    start: The starting index (default is 0).

How It Works
    The enumerate() function produces a sequence of tuples, where:

    The first element of each tuple is the index.
    The second element is the value from the iterable.
"""

# example: Enumerating a List
mylist = [1, 2, 3, 4, 5]
print(enumerate(mylist))  # <enumerate object at 0x72d84952c540>
enumerated_list = list(enumerate(mylist))
print(enumerated_list)  # [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
for index, value in enumerate(mylist):
    print(f"Index: {index}, Value: {value}")

# output
# Index: 0, Value: 1
# Index: 1, Value: 2
# Index: 2, Value: 3
# Index: 3, Value: 4
# Index: 4, Value: 5


# example: starting index from 1 not 0
enumerated_list_of_index_1 = enumerate(mylist, start=1)
print(list(enumerated_list_of_index_1))  # [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]


# example: using enumerate() with a string
string = 'hello world!'
stringenumerated = enumerate(string)
print(list(stringenumerated))  # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'w'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd'), (11, '!')]


# example: enumerating a tuple
mytuple = (1, 2, 3, 4,)
mytupleEnumerated = enumerate(mytuple)
print(mytupleEnumerated)  # # enumerate object
print(tuple(mytupleEnumerated))  # ((0, 1), (1, 2), (2, 3), (3, 4)
print(list(mytupleEnumerated))  # []
print(set(mytupleEnumerated))  # set()
print(dict(mytupleEnumerated)) # {}

"""
The reason the last three lines (list(mytupleEnumerated), set(mytupleEnumerated), and dict(mytupleEnumerated)) print empty collections is because the enumerate object is exhausted after the first iteration when you convert it to a tuple.

Key Concept: Iterators and Exhaustion
    The enumerate() function returns an iterator.
    Iterators in Python can only be iterated over once. After that, they are "exhausted" and cannot produce any more values.
    When you first convert mytupleEnumerated into a tuple, it consumes all the elements of the enumerate object.
    Subsequent attempts to convert or iterate over mytupleEnumerated (e.g., using list(), set(), or dict()) find nothing left, as the iterator is already exhausted.

To avoid that, we have 2 solutions

    1. create the enumerate object each time
        mytuple = (1, 2, 3, 4)
        print(tuple(enumerate(mytuple)))  # ((0, 1), (1, 2), (2, 3), (3, 4))
        print(list(enumerate(mytuple)))  # [(0, 1), (1, 2), (2, 3), (3, 4)]
        print(set(enumerate(mytuple)))   # {(0, 1), (1, 2), (2, 3), (3, 4)}
        print(dict(enumerate(mytuple))) # {0: 1, 1: 2, 2: 3, 3: 4}

    2. Store the Result of the Conversion in a Variable: Convert the enumerate object to a collection (like a tuple, list, etc.) once and use that variable multiple times:
        mytuple = (1, 2, 3, 4)
        enumerated_tuple = tuple(enumerate(mytuple))
        print(enumerated_tuple)        # ((0, 1), (1, 2), (2, 3), (3, 4))
        print(list(enumerated_tuple))  # [(0, 1), (1, 2), (2, 3), (3, 4)]
        print(set(enumerated_tuple))   # {(0, 1), (1, 2), (2, 3), (3, 4)}
        print(dict(enumerated_tuple))  # {0: 1, 1: 2, 2: 3, 3: 4}

Key Takeaways
    - Iterators can only be iterated over once.
    - Once an iterator is exhausted, trying to iterate over it again results in an empty sequence.
    - To reuse an enumerate object, either recreate it or store its contents in a reusable collection.
"""

"""
The enumerate() function returns an iterator, which behaves similarly to generators in the sense that it lazily generates values one by one. However, the way you access these values differs from using the next() function.

Key Points of enumerate() as an Iterator:

Iterator Behavior:
    - enumerate() converts an iterable (like a list or tuple) into an iterator.
    - It doesn’t store the values in memory all at once, instead, it generates them lazily, one at a time, as you iterate over it.
    - After you exhaust it (i.e., iterate through all elements), you can’t retrieve the values again unless you create a new enumerate object.

Difference from Generators:
    - Generators are a specific type of iterator that you define using functions with yield or generator expressions. They generate values lazily when called.
    - enumerate() is not a generator in the sense that you don't define it with yield, but it still behaves like one because it generates values lazily as you iterate.

No Need for next():
    - When you use enumerate(), you don’t manually call next() to get each element. Instead, you iterate over it directly in a loop, which automatically retrieves the next item.
    - If you wanted to manually get items from an enumerate() iterator, you could use next(), but it’s usually not necessary since loops handle this automatically.

Example with next() and enumerate()
You can manually get items from an enumerate() object by using next():

fruits = ['apple', 'banana', 'cherry']
enumerated_fruits = enumerate(fruits)

# Manually getting items with next()
print(next(enumerated_fruits))  # (0, 'apple')
print(next(enumerated_fruits))  # (1, 'banana')
print(next(enumerated_fruits))  # (2, 'cherry')

After you’ve called next() for all items, further calls to next() will raise a StopIteration exception because the iterator is exhausted.
"""

"""
Key Points
    enumerate() is useful when you need both the index and the value during iteration.
    It makes code more readable and concise compared to manually maintaining an index counter.
"""