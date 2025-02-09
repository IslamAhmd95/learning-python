# dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band_2 = dict(vocals= "Plant",
    guitar= "Page")

band_3 = dict({"vocals": "Plant",
    "guitar": "Page"})

print(band, band_2, band_3)  # {'vocals': 'Plant', 'guitar': 'Page'} {'vocals': 'Plant', 'guitar': 'Page'} {'vocals': 'Plant', 'guitar': 'Page'}

d = [["name", "Islam"], ["age", 28], ["gender", "Male"]]
print(dict(d))  # {'name': 'Islam', 'gender': 'Male', 'age': 28}
d = [("name", "Islam"), ("age", 28), ("gender", "Male")]
print(dict(d))  # {'name': 'Islam', 'gender': 'Male', 'age': 28}
d = {("name", "Islam"), ("age", 28), ("gender", "Male")}
print(dict(d))  # {'name': 'Islam', 'gender': 'Male', 'age': 28}

keys = ('name', 'gender', 'age')
values = ('Islam', 'Male', 28)
pairs = zip(keys, values)
print(pairs)  # <zip object at 0x765bbad45b00>
# print(dict(pairs))  # {'name': 'Islam', 'gender': 'Male', 'age': 28}
# print(list(pairs))  # [('name', 'Islam'), ('gender', 'Male'), ('age', 28)]
print(tuple(pairs))  # (('name', 'Islam'), ('gender', 'Male'), ('age', 28))


keys = ('a', 'b', 'c')
defaultValue = 0
print(dict.fromkeys(keys, defaultValue))  # {'a': 0, 'b': 0, 'c': 0}

# you can use any object of immutable types as dictionary keys - such as numbers, strings booleans or tuples but values can be any types


d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d['a']) # 1, throw an error if key doesn't exist
print(d.get('a')) # 1, return none if key doesn't exist



# access items
print(band['guitar'])
print(band.get('vocals'))

# list all keys
print(band.keys())  # dict_keys(['vocals', 'guitar'])

# list all values
print(band.values())  # dict_values(['Plant', 'Page'])

# list all key/value pairs as tuples
print(band.items())  # dict_items([('vocals', 'Plant'), ('guitar', 'Page')])

# verify key 
print('guitar' in band) # True

# change value
band["vocals"] = "Gibson"
band.update({"bass": "JPJ"}) # add the key/value if not existing
print(band)

# remove items
print(band.pop("bass"))  # returns only the value
print(band)  # the bass:JPJ is removed

band["drums"] = "Bonham"
print(band.popitem()) # remove the last key/value pair then returns them as a tuple
print(band)

# delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band_2.clear() # clear the band
print(band_2)
del band_2

# Copy dictionary
band_2 = band  # create a reference to band dict, means both referring to the same place in memory and if you updated one of them, the other will be updated too, so this is not a copy operation
band_2 = band.copy()
band_2["updated"] = True
print(band, band_2)

band_2 = dict(band)  # another way to copy dict, using the dict constructor function
print(band, band_2)


# Nested dictionary
member1 = {
    "name": "islam",
    "age": 29
}

member2 = {
    "name": "mohamed",
    "age": 26
}

members = {
    "member1": member1,
    "member2": member2
}

print(members)
print(members["member1"]["name"])
print("name" in member1)  # True
for key in member1:
    print(key + " " + str(member1[key]))



# ----------------------------------------------------------------



## Sets

"""
Sets are unordered - items stored in a set are not kept in a particular order
Sets are unidexed - we can't access set items by index
Set items are unique - duplicated items are not allowed
Sets are changeable (mutable) - they can be changed, shrinked or growed on demand
The set itself is mutable, but it can't contain mutable items like lists or dictionaries but can contain immutable items like numbers, strings or tuples
"""

nums = {1, 2, 3, 4, 5, 6, 7, 8}
nums2 = set({1, 2, 3})
print(nums2)
print(type(nums), type(nums2))

# No duplicates are allowed
nums = {1, 2, 2, 3}
print(nums)  # {1, 2,3} it ignored the duplicates and didn't produce an erorr

print(True + 1)    # Output: 2 (True is treated as 1 which is dupe "مطابق" of True)
print(False + 10)  # Output: 10 (False is treated as 0 which is dupe "مطابق" of False)

nums = {1, True, False, 2, 4, 0}
print(nums)  # Output {false, 1, 2, 4} True is the same as 1 and 1 comes first so it's 1 and the same for false

# check if value is in set
print(2 in nums)

# but you can't refer to an element in the set with the index like the list or the tuple or with a key like dictionary

# add values to set
nums.add(9)
print(nums)
nums.remove(9) # remove only one item, raise error if item doesn't exist
nums.discard(9) # remove only one item, doesn't raise error if item doesn't exist
removed_item = nums.pop()
print(removed_item)

morenums = {6, 7, 10}
nums.update(morenums)  # add multiple values at once
print(nums)
# you can use update() with lists, tuples and dictionaries also
nums.update([12, 13, 13])
print(nums)  # {False, 1, 2, 4, 6, 7, 9, 10, 12, 13}

nums.update((14, 15, 16))
print(nums)  # {False, 1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 16}
# nums.clear() # clear the set 

nums.update({17, 18, 19})

my_dict = {'a': 10, 'b': 20, 'c': 30}

nums.update(my_dict)  # Adds the keys of the dictionary to the set
print(nums)  # Output: {False, 1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 16, 'a', 'b', 'c'}


a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))  # True , Checks if all elements of one set are in another.
print(b.issuperset(a))  # True  ,   Checks if a set contains all elements of another set.

a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b)) # True , Checks if two sets have no elements in common.


set1 = {1, 2, 3}
set_copy = set1.copy()
print(set_copy)  # Output: {1, 2, 3} , Creates a shallow copy of the set.

s = {1, 2, 3}
print(len(s))  # Output: 3, get length of set

# Set comprehension
s = {x**2 for x in range(5)}
print(s)  # Output: {0, 1, 4, 9, 16}


## Set Operations


# Union  "|"
# The union of two sets A, B is all items on the A, B 
nums1 = {1, 2, 3}
nums2 = {4, 5, 6}
mergedSet = nums1.union(nums2)  # nums1 | nums2
print(mergedSet)  # {1, 2, 3, 4, 5, 6}


# Union update
# no function for union update but i can perform it with this symbol "|="
# The union of two sets A, B is all items on the A, B 
nums1 = {1, 2, 3}
nums2 = {4, 5, 6}
nums1 |= nums2  # nums1 |= nums2
print(nums1)  # {1, 2, 3, 4, 5, 6}


# Intersection  "&"
# Returns a new set containing the intersection of the sets involved.
# Does not modify the original set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.intersection(set2)
print(result)  # Output: {3, 4}
print(set1)    # Output: {1, 2, 3, 4}  (unchanged)


# intersection_update  "&="
# Modifies the original set in place by keeping only the intersection of the sets.
# Does not return a new set (returns None).
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2)
print(set1)  # Output: {3, 4}  (modified)


# symmetric_difference()  "^"
# The symmetric difference between A, B is the set of all items that in either A or B but not in both.
# Returns a new set containing the symmetric difference of the sets.
# Does not modify the original set.
# it's equal to Union  - Intersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.symmetric_difference(set2)
print(result)  # Output: {1, 2, 5, 6}
print(set1)    # Output: {1, 2, 3, 4} (unchanged)


# Symmtric difference update  "^="
# Modifies the original set in place by keeping only the symmetric difference.
# Does not return a new set (returns None).
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 5, 6} (modified)



# Difference  "-"
# The difference between 2 sets A, B is the items in A but not in B.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.difference(set2))  # Output: {1, 2}


# Difference update  "-="
# Updates the original set with the difference.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.difference_update(set2) 
print(set1)  # {1, 2}


#----------------------------------------------------------------

# Frozenset

# Immutable: Elements cannot be added or removed after creation.
# Hashable: Because it is immutable, a frozenset can be used as a key in a dictionary or added to a set (which requires hashable elements).
# Order is not guaranteed: Like a set, the elements in a frozenset have no specific order.
# Unique elements: Duplicate elements are automatically removed, just like in a regular set.
# Use frozenset to create a set that cannot be accidentally modified
# frozenset supports the same set operations that create a new set (like union, intersection, etc.).
# frozenset does not support operations that modify the set in place (like add or remove).


# Creating a frozenset
fs = frozenset([1, 2, 3, 4, 4])  # Duplicate 4 is ignored
print(fs)  # Output: frozenset({1, 2, 3, 4})


my_set = set()
my_dict = {'a': 10, 'b': 20}
my_set.add(frozenset(my_dict.items()))
print(my_set)  # Output: {frozenset({('a', 10), ('b', 20)})}


# fs = frozenset([1, 2, 3])
# fs.add(4)  # Error: frozenset is immutable


# Since frozenset is hashable, it can be used as a dictionary key.
my_dict = {frozenset([1, 2, 3]): 'value1', frozenset([4, 5, 6]): 'value2'}
print(my_dict)  # Output: {frozenset({1, 2, 3}): 'value1', frozenset({4, 5, 6}): 'value2'}


# Frozenset can also be used as a set element.
my_set = {frozenset([1, 2, 3]), frozenset([4, 5, 6])}
print(my_set)  # Output: {frozenset({1, 2, 3}), frozenset({4, 5, 6})}

