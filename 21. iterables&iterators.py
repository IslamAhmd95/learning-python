"""
Iterable vs. Iterator


Analogy to Understand Iterables and Iterators
    Imagine you have a book (an iterable) that contains multiple pages.
    The book itself cannot directly tell you what's on the next page, but you can use a bookmark (an iterator) to read it page by page.
    The bookmark remembers which page you are on, and each time you move it, it gives you the next page.
    Once you reach the last page, the bookmark will tell you there's nothing left to read (this is like a StopIteration error in Python).
    Iterable: The book (list, string, dictionary, etc.).
    Iterator: The bookmark (something that lets you go through the book step by step).
    iter(): Creates a bookmark from the book.
    next(): Moves the bookmark to the next page and shows its content.

Iterable
    An iterable is any object capable of returning its elements one at a time.
    Examples of iterables include collections like lists, tuples, dictionaries, and sets.
    An iterable must implement the __iter__() method, which returns an iterator.
    You can use a for loop with an iterable.

Iterator
    An iterator is an object that represents a stream of data. It lets you access elements of the iterable one at a time.
    An iterator must implement:
    __iter__() (which returns the iterator itself, ensuring compatibility with for loops).
    __next__() (which returns the next item in the sequence or raises StopIteration if the sequence is exhausted).
    You can use next() with an iterator.

Relationship Between Iterable and Iterator
    Calling iter() on an iterable returns an iterator.
    Calling iter() on an iterable does not change the iterable itself. It simply creates an iterator.
    Iterators maintain a state to remember their position in the sequence, while iterables do not.

Difference Between Iterable and Iterator
    An iterable is an object that implements the __iter__ method, returning an iterator. Examples include lists, tuples, dictionaries, and custom classes with __iter__.
    An iterator is an object that implements both the __iter__ and __next__ methods. It keeps track of its position during iteration.

Key Methods

iter() Function
    Converts an iterable (like a list) into an iterator.
    Can also be called on an iterator, but it simply returns the iterator itself.

next() Function
    Retrieves the next item from an iterator.
    Raises StopIteration when no more items are left.

__getitem__() Method
    Allows an object to behave like a collection, supporting index-based access.
    If an object implements __getitem__(), Python treats it as an iterable.

Practical Notes
    You use iter() to convert an iterable to an iterator to access elements one by one using next().
    Using iter() on an iterator does nothing; it simply returns the same iterator.
    The for loop internally uses the iter() function to obtain an iterator from an iterable and next() to loop through its elements.

"""

mylist = [1, 2, 3]  # iterable
mylistiterator = iter(mylist)  # iterator
print(mylistiterator) # <list_iterator object at 0x790163d340a0>
print(next(mylistiterator)) # 1
print(next(mylistiterator)) # 2
print(next(mylistiterator)) # 3
# print(next(mylistiterator)) # raise StopIteration exception


#  custome iterators
# You can create your own iterator by defining a class with __iter__() and __next__() methods.
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            result = self.current
            self.current += 1
            return result
        

counter = Counter(1, 5)
print(counter.__next__()) # 1
print(counter.__next__()) # 2
print(next(counter))  # 3, the under method __next__ can be used like the built-in next(), and not all the dunder methods has a corresponding built-in function
# print(counter.__next__()) # 4
# print(counter.__next__()) # 5
# print(counter.__next__()) # stop iteration error
for num in counter:  # # Works because of __iter__()
    print(f"Number is {num}") #  Number is 4, Number is 5

# iterators always remembers it's current state, so when the for loop started it remembers it stopped at 3 and continued from 4, explained below in depth

"""
explanation for the counter class

    You created an iterator manually by implementing:
        __iter__: Makes the class iterable. Since the class itself is an iterator, you return self.
        __next__: Defines how to fetch the next item from the sequence. This is where you maintain the "state" (e.g., self.current).
    Once the class is instantiated, calling iter(counter_instance) just returns the instance itself (because of __iter__).
    You can then use the built-in next(counter_instance) or the dunder method counter_instance.__next__() to fetch the next item one by one, or simply iterate using a for loop, which automatically uses __iter__ and __next__.
"""
#----------------------------------------------------------------

"""
What Happens in a for Loop?

    A for loop is not an iterator itself, but it uses iterators internally.
    When you write for item in iterable:, Python automatically:
    Calls iter() on the iterable to create an iterator.
    Calls next() on the iterator in each loop iteration.
    Stops when it encounters a StopIteration error.
"""
numbers = [1, 2, 3, 4]
for x in numbers:
    print(x)

#  working the same like the below example

numbersIterator = iter(numbers)
while True:
    try:
        print(next(numbersIterator))
    except StopIteration:
        print("All items have been processed")
        break


#----------------------------------------------------------------

"""
__getitem__() is a special method in Python that allows objects to support the indexing operation, like accessing elements in a list or dictionary.

It allows you to make objects "subscriptable," meaning you can access individual items by their index or a slice of items.

When you use square brackets ([]) to access an element, Python internally calls the __getitem__() method on the object.

How It Works
If an object implements the __getitem__() method, it can be treated as a subscriptable object, meaning you can use indexing (object[index]) to retrieve elements.
"""


"""
Handling Slicing with slice Objects
    When you use slicing syntax (e.g., collection[1:4:2]), Python doesn't pass multiple arguments to __getitem__. Instead:

    Python creates a slice object that represents the start, stop, and step values of the slice.
    This slice object is passed as the single index argument to __getitem__.

    The slice object is a type, just like int or str. That's why isinstance(index, slice) works:
"""

s = slice(1, 4, 2)  # Equivalent to [1:4:2]
print(s.start) # 1
print(s.stop)  # 4
print(s.step)  # 2

print(isinstance(s, slice))  # True


# example on getitem with slicing
class MyCollection:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        if isinstance(index, str):
            return self.data.get(index, "Key not found")
        
        if isinstance(index, slice):
            return self.data[index.start:index.stop:index.step]
        
        # if index > len(self.data):
        #     raise IndexError("Index is out of range")
        
        # return self.data[index]
        if isinstance(index, int):
            try:
                return self.data[index]
            except IndexError:
                return "Index Error: index is out of range"
            
        raise TypeError("Invalid index type")
    

mycollection = MyCollection([1, 2, 3, 4, 5, 6])
# mycollection = MyCollection((1, 2, 3, 4, 5, 6))
# print(mycollection[10])  # IndexError: Index is out of range
print(mycollection[1]) # 2, The __getitem__() method is called whenever you use mycollection[index].
print(mycollection.__getitem__(1))  # 2
# print(mycollection[[1]])  # TypeError: Invalid index type
print(mycollection[0:5:2])  # [1, 3, 5]
print(mycollection[:])  # [1, 2, 3, 4, 5, 6] (Equivalent to a shallow copy)

mycollection = MyCollection({'a': 1, 'b': 2})
print(mycollection['a'])  # 1
print(mycollection['c'])  # Key not found


#----------------------------------------------------------------

""""
When you call iter() on an iterator, it simply returns the same iterator object. This ensures compatibility with Python's iteration protocol.

In Python, objects that can be iterated over must provide an __iter__() method, which returns an iterator.
Iterators implement __iter__() and return themselves when iter() is called. This ensures they can be used smoothly in loops or other places requiring an iterable.
"""

myIterator = iter([1, 2, 3])
print(iter(myIterator) is myIterator)  # True 

#----------------------------------------------------------------

"""
Why convert an iterable (like a list) to an iterator?

You might not always need to convert an iterable to an iterator explicitly, as Python does this automatically in loops. However, there are situations where you need manual control over the iteration process, which requires an iterator.

Use Cases for Converting an Iterable to an Iterator:

    Custom Iteration Logic:
    You can manually control how and when to get the next element.
    Example:
        my_list = [1, 2, 3]
        iterator = iter(my_list)
        print(next(iterator))  # Output: 1
        print(next(iterator))  # Output: 2

    Lazy Evaluation:
    Iterators process one element at a time, which can save memory for large data.
    Example:
        my_large_list = range(1, 1_000_000)  # Iterable
        iterator = iter(my_large_list)  # Iterator
        print(next(iterator))  # Only processes the first element

    Integration with Other Functions:
        Some Python functions (e.g., zip, map, filter) return iterators, and you might need to convert iterables to iterators to work smoothly with these.

    Custom Iteration Objects:
        When you create your own iterable classes, you may need to implement the __iter__() method, which must return an iterator. This might involve explicitly converting internal data to an iterator.

"""

#----------------------------------------------------------------

class CombinedObject:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        if isinstance(index, str):
            return self.data.get(index, "Key not found")
        
        if index > len(self.data):
            raise IndexError('Index is out of range')
        
        return self.data[index]
    
    def __iter__(self):
        return iter(self.data)
    


combinedObject = CombinedObject([1, 2, 3, 4, 5])
print(combinedObject[2])
print(combinedObject.__getitem__(2))
# combinedObjectIterator = iter(combinedObject)  # the same like the below one
combinedObjectIterator = combinedObject.__iter__()
print(next(combinedObjectIterator))  # 1 , I need to run iter method first before using next method
print(next(combinedObjectIterator))  # 2
for item in combinedObjectIterator:
    print(f"{item} of the combined object") # 3, 4, 5

"""
Explanation for the combinedObject class

    The class itself is not inherently an iterator because it doesn’t implement __next__.
    Instead, you implemented the __iter__ method, which:
        Converts the internal self.data (an iterable, like a list or dictionary) into an iterator using the built-in iter() function.
        Returns this iterator.
    After calling iter(combined_instance), you can now use the built-in next() method on the returned iterator.
    If you try next(combined_instance) directly without calling iter(combined_instance), it will raise a TypeError because combined is an iterable, not an iterator.
"""

#----------------------------------------------------------------


"""
Iterators maintain a state to remember their position in the sequence, while iterables do not.

Iterables
    Iterables do not track their position in the sequence because they are just collections of data.
    When you create an iterator from an iterable using iter(), you can traverse the sequence. However, the iterable itself doesn't "remember" where you left off.
    Example:
        data = [1, 2, 3]  # This is an iterable (list)

        iterator1 = iter(data)  # Create an iterator
        iterator2 = iter(data)  # Create another iterator

        print(next(iterator1))  # Output: 1
        print(next(iterator1))  # Output: 2

        print(next(iterator2))  # Output: 1  (A new iterator starts from the beginning)
        Here, the iterable (data) doesn’t track any state—every time you call iter(), a new iterator is created starting from the first element.

Iterators
    Iterators track their position because they maintain an internal state, usually via the __next__() method.
    Every time you call next() on an iterator, it "remembers" where it left off and returns the next item in the sequence.

"""

# How Iterators Maintain State
# Internally, an iterator object typically maintains a pointer or index that indicates its current position within the sequence. Each time next() is called, this pointer is updated.

# Here’s a simplified custom implementation of an iterator:

class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0  # Maintains the position in the sequence

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index > len(self.data):
            raise StopIteration
        
        result = self.data[self.index]
        self.index += 1
        return result
    

# Example usage
iterator = CustomIterator([10, 20, 30])

print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30
# print(next(iterator))  # Raises StopIteration