# Dictionary Comprehension

d = {x:x**2 for x in range(5)}
print(d)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

d = {x:x*3 for x in 'RED'}
print(d)  # {'R': 'RRR', 'E': 'EEE', 'D': 'DDD'}

colors = ['red', 'green', 'blue']
d = {x.lower():x.upper() for x in colors}
print(d)  # {'red': 'RED', 'green': 'GREEN', 'blue': 'BLUE'}

d = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
selectKeys = [0, 2, 4, 6]
selectedDict = {x:d[x] for x in selectKeys}
print(selectedDict)  # {0: 'a', 2: 'c', 4: 'e', 6: 'g'}

removedKeys = [1, 3, 5, 7]
filteredDict = {x:d[x] for x in d if x not in removedKeys}
print(filteredDict)  # {0: 'a', 2: 'c', 4: 'e', 6: 'g', 8: 'i', 9: 'j'}
filterDict = {x:d[x] for x in d.keys() - removedKeys}
print(filteredDict) # {0: 'a', 2: 'c', 4: 'e', 6: 'g', 8: 'i', 9: 'j'}


# Reverse lookup
# Given a dictionary d and the key k, it's easy to find the value of v = k with d[k], this operation is called lookup, but if i want to get the key of a value in the dictionary , this opertion is called reverse lookup

d = {0: 'a', 1: 'b', 2: 'c'} 
print(type(d.items()))  # <class 'dict_items'>
print(d.items())  # dict_items([(0, 'a'), (1, 'b'), (2, 'c')])
d = {k:v for v, k in d.items()}  # swapping keys and values
print(d)  # { 'a': 0, 'b': 1, 'c': 2 }


colors = ["red", "green", "blue"]
d = {color: i for i, color in enumerate(colors)}
print(d)  # {'red': 0, 'green': 1, 'blue': 2}



# Nested dictionary comprehension
d = {(x, k): x+k for x in range(2) for k in range(3)}   # {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 1, (1, 1): 2, (1, 2): 3}

# this is equivalent to the following code

# d = dict()
# for x in range(2):
#     for k in range(3):
#         d[(x, k)] = x + k;

print(d)