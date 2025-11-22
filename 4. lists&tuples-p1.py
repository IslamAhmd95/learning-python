## Lists

"""
Lists are orders, changeable and allow duplicate values.
List comprehension is a way to create lists based on an existing list
The relationship between indices and values is called mapping, each index map to a value
"""

users = ['Dave', 'John', 'Sara']
emptyList = []

print(users[-1])
print(users[0:-2])
print(len(users))
print(users.index('Sara'))

users.append('Elsa') # add item to the end of the list
users += ['John', 'Sara'] # to the end of the list
# users.extend(['scarlet', True, 42]) # to the end of the list
print(users)

users.insert(1, 'Bob') # insert item at position 1
users[2:2] = ['iddie'] # No elements are replaced; new element is inserted at index 2
users[3:4] = ['alice'] # The element at index 3 is replaced by the new element (['alice']).
print(users)

users.remove('Sara') # removes the first occurrence of 'Sara'
print(users.pop()) # get the last element of the list and remove it from the list
print(users)
# y = users.pop(3)  # get the element of index 3 and remove it from the list

del users[2] # remove the element at index 2  
# del users[1:3] # delete multiple items from the list
del emptyList # delete the list 
# print(emptyList)  # error message, the list is not defined 
# users.clear() # clear the list
# print(users)

users.sort() # sort the users alphabetically, lower case comes at the end
print(users)

users.sort(key=str.lower) # sort the users alphabetically, lower case names come at their order 
print(users)

nums = [3,4,7,1,32,8,0,21,42]
nums.reverse() # reverse the nums list
nums.sort() # sort the nums ascending
# nums.sort(reverse=True) # sort the numbers in descending order

print(sorted(nums, reverse=True)) # sort the numbers in descending order but keep the original list
print(nums)

# 3 ways to copy the list, the copy is a completely different list
numsCopy_1 = nums.copy()
numsCopy_2 = list(nums)
numsCopy_3 = nums[:]

newList = list([1, 2, True, 'islam'])
print(type(newList)) # <class 'list'>

oldlist = [1, 2, 3]
newlist = oldlist * 2 # duplicate the nums list items in nums2 lists
print("newlist")
print(newlist) # [1, 2, 3, 1, 2, 3]

boolList = [True, False, False]
print(all(boolList)) # False, all must be true
print(any(boolList)) # True, one true is enough

# list slicing
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list[start:stop:step]
print(x[::-1]) # reverse the list
"""
Explanation of x[::-1]:
Start index: Not specified, defaults to the start of the list.
End index: Not specified, defaults to the end of the list.
Step: -1 means move backward through the list.
"""
print(x[-6:-1:2]) # [5, 7, 9]
print(x[-6:-1:-2]) # []
print(x[-1:-6:-2]) # [10, 8, 6], negative steps meaning moving backwards, so the start index should be on the right and of the end index 
print(x[1:6:-2]) # []
print(x[-1:]) # [10]
"""
Explanation of x[-1:]:

Start index (-1):
Refers to the last element of the list (10).

End index (None):
No value after the colon means go to the end of the list.
Start index (-1):
Refers to the last element of the list (10).

End index (:):
No value after the colon means go to the end of the list.

Default step (+1):
The default step is forward, so it slices the list from the last element to the end of the list.
"""
x[:0] = ['a', 'b'] # add list the beginning of the list
print(x)
x[len(x):] = ['c', 'd'] # add list the end of the list
print(x)
del x[2:5]  # delete multiple items from the list
# x[2:5] = []  same thing
print(x)


"""
Shallow Copy:
    A shallow copy creates a new object but does not recursively copy the objects inside it. Instead, it references the same nested objects.
    Changes to the inner objects will affect both the original and the copied object since they share the same references.

    Shallow Copy Behavior
        Outer list: 
        A new list object is created with a different memory address.
        Inner objects:
        The shallow copy does not create new copies of the inner objects. Instead, it copies the references (memory addresses) of the inner objects from the original list.
        This means the original and the copied lists share the same inner objects.

    x[0] and y[0] have the same memory address 0x7f...abcd
    So, if you modify y[0][0], the change is reflected in x[0][0] because they point to the same inner object.
"""
y = x[:] # When you do y = x[:], Python creates a new list object for y that contains references to the same inner objects as x. The memory address of the outer list (container) for y is different from that of x.
print(y == x)  # True, checks if the values in `y` and `x` are the same
print(y is x)  # False, checks if `y` and `x` are the same object in memory, the outer lists are different objects but they just share the inner objects 
print(y[0] is x[0])  # True, the inner ojects are the same

x = [[1, 2], [3, 4]]
y = x[:]  # Shallow copy

y[0][0] = 99  # Modifies the inner list
print(x)  # [[99, 2], [3, 4]] (inner object is shared)


"""
Deep Copy:
    A deep copy creates a new object and recursively copies all objects inside it.
    The copied object and the original object are entirely independent, including their nested objects.

    Deep Copy Behavior
        Outer list: 
        A new list object is created with a different memory address.
        Inner objects:
        The deep copy recursively copies all nested objects, creating new objects for each level.
        The original and the copied lists (and all their nested objects) are completely independent.
"""
import copy

x = [[1, 2], [3, 4]]
y = copy.deepcopy(x)  # Deep copy
y[0][0] = 99  # Modifies the inner list
print(y) # [[99, 2], [3, 4]]
print(x) # [[1, 2], [3, 4]]



print("end of lists")

#----------------------------------------------------------------


## Tuples

# Once a tuple is created, its elements cannot be changed, added, or removed, This is what makes tuples immutable.

# Like lists, tuples maintain the order of elements. The order in which you define the tuple is preserved.

myTuple = (1, 2, 5, 33, 77, 2)
anotherTuple = ('Dave', 'Elsa', ' John')

print(myTuple[0]) # print the first element
print(myTuple[-1]) # print the last element
print(type(anotherTuple))

t = 1, "a", True
print(t)  # (1, 'a', True), you don't need parentheses to make a tuple

t = (4,)
print(t, type(t))  # (4,) <class 'tuple'>, if tuple has one item, we must use comma

t = (4)
print(t, type(t))  # 4 <class 'int'>    


"""
1. Tuple Packing
    Packing is the process of grouping multiple values into a single tuple.
    # Packing values into a tuple
    packed_tuple = 1, 2, 3
    print(packed_tuple)  # Output: (1, 2, 3)

    You can remove parentheses when packing values into a tuple.
    Multiple values separated by commas automatically form a tuple.


2. Tuple Unpacking
    Unpacking is the process of extracting values from a tuple into individual variables.
    # Unpacking values from a tuple
    a, b, c = packed_tuple  # packed_tuple = (1, 2, 3)
    print(a)  # Output: 1
    print(b)  # Output: 2
    print(c)  # Output: 3

    The number of variables on the left must match the number of elements in the tuple.


3. Packing and Unpacking Together
    Tuple packing and unpacking can happen simultaneously.
    # Packing and unpacking in one step
    a, b, c = 1, 2, 3
    print(a, b, c)  # Output: 1 2 3


4. Advanced Unpacking with * (Extended Unpacking)
    You can use * to capture multiple elements during unpacking, works with any iterable (list, tuple, string, set, dictionary ..)
    # Packing and unpacking with *
    t = (1, 2, 3, 4, 5)

    # Unpack with *
    a, *middle, e = t
    print(a)       # Output: 1
    print(middle)  # Output: [2, 3, 4]
    print(e)       # Output: 5

    # Using * with a dictionary
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    key, *rest = my_dict
    print(key)     # Output: 'a'
    print(rest)    # Output: ['b', 'c']

    # Unpacking values
    *values = my_dict.values()
    print(values)  # Output: [1, 2, 3]

    # Using * with a set
    my_set = {1, 2, 3, 4, 5}
    first, *rest = my_set
    print(first)  # Output: (Could be any element because sets are unordered)
    print(rest)   # Output: (A random collection of elements)

    If the unpacked value is a single element, it will be assigned directly to the variable (not wrapped in a list).
    If multiple elements are unpacked, they will be stored as a list (or tuple depending on the context, but by default, it is a list).


    The * variable captures any remaining values as a list, if no elements the list is empty


5. Use Cases

    - Swapping
        # Swap two variables using tuple unpacking
        a, b = 5, 10
        a, b = b, a
        print(a, b)  # Output: 10 5

    - Returning multiple values from a function
        def get_coordinates():
            return 10, 20  # Tuple packing

        x, y = get_coordinates()  # Tuple unpacking
        print(x, y)  # Output: 10 20

    - Looping with Unpacking
        # Unpacking tuples in a loop
        pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
        for num, name in pairs:
            print(num, name)
        # Output:
        # 1 one
        # 2 two
        # 3 three

"""
(one, *two, three) = myTuple
print(one) # first element
print(two) # the elements on the middle packed into a list
print(three) # last element

email = "Islam@gmail.com"
name, domain = email.split("@")
print(name, domain)


# if we want to add a new element to the tuple
newList = list(myTuple)
newList.append(42)
newTuple = tuple(newList)
print(newTuple)


print(myTuple.count(2)) # count the number of occurrences of 2 on the tuple


# Tuple slicing is similar to list slicing
t = (1, 2, 3, 4, 5, 6, 7, 8)
tSliced = t[1:5:2]
print(tSliced)  # Output: (2, 4)


# Tuples are immutable but can have mutable values
t = ([1, 2, 3], "a")
# t[1] = "b"   # TypeError: 'tuple' object does not support item assignment
t[0][1] = "b"
print(t)  # Output: ([1, "b", 3], "a")


t = ("c", "b", "a", "d")
print(sorted(t)) # ['a', 'b', 'c', 'd']
print(sorted(t, reverse=True)) # ['d', 'c', 'b', 'a']
print(sorted((5, 23, 6, 99, 0, 4)))  # [0, 4, 5, 6, 23, 99]
print(sorted((5, 23, 6, 99, 0, 4), reverse=True))  # [99, 23, 6, 5, 4, 0]