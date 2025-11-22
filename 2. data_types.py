import math

## Strings

# literal assignment
first = "islam"
last = "ahmd"
print(type(first)) # <class 'str'>
print(type(first) == str)  # True
print(isinstance(first, str)) # True


# constructor assignment
first = str("islam")
print(type(first)) # <class 'str'>
print(type(first) == str)  # True
print(isinstance(first, str)) # True


# concatenation
fullname = first + " " + last
fullname += "!"
print(fullname)  # islam ahmd!


# casting a number to a string
decade = str(1980)
print(type(decade)) # <class 'str'>
statment = "I love rock music from " + decade + "s."
print(statment)  # I love rock music from 1980s.


# multiple lines
multilines = '''
I'm islam  
    I love soccer
           and movies

'''
print(multilines) 


# escape characters
sentence = 'I\'m back from work.\t\t Hey!\n\n where\'s at\\located?'
print(sentence) 


# string functions
print(first.lower()) # islam
print(first.upper()) # Islam
print(sentence.title()) # returns a copy of the string where the first letter of each word is capitalized,
print(len(first))
print(sentence.replace('work', 'home'))
sentence += "                 "  # space added to end of string
sentence = "                     " + sentence   # space added to the start of string
print(sentence.strip())  # remove leading and trailing spaces
print(sentence.lstrip()) # remove leading spaces
print(sentence.rstrip()) # remove trailing spaces


# build a menu
title = "menu".upper()
print(title.center(20, "="))  # ========MENU========
print("coffee".ljust(16, ".") + "$1".rjust(4))  # coffee..........  $1


# string index values
print(first[1])
print(first[-1])  # the last character in case we don't know the lendth
print(first[0:len(first)])  #islam
print(first[0:])  # islam
print(first[0:-1])  # isla


# Methods return beturns boolean values
print(first.startswith("i"))  # True
print(first.endswith("m"))  # True


## Booleans
myValue = True
anotherValue = bool(False)  # constructor way
print(type(myValue)) # <class 'bool'>
print(isinstance(anotherValue, bool)) # True


## Numberic data types


# integers
x = 10
y = int(20)
print(type(x)) # <class 'int'>
print(isinstance(y, int)) # True


# floats
gpa = 3.28
z = float(10)
print(type(gpa)) # <class 'float'>
print(isinstance(z, float)) # True
print(z)  # 10.0


# complex numbers
a = 1 + 2j
print(type(a)) # <class 'complex
print(a.real) # 1.0
print(a.imag) # 2.0, imag stands for imaginary


# built-in functions for numbers
print(abs(-5))  # 5, The absolute value is the non-negative value of a number, regardless of its sign
print(max(1, 2, 3, 4, 5))  # 5
print(min(1, 2, 3, 4, 5))  # 1
print(pow(2, 3))  # 8
print(round(3.75))  # 4
print(round(3.75, 1))  # 3.8

print(math.ceil(3.75))  # 4
print(math.floor(3.75))  # 3    
print(math.sqrt(16))  # 4.0
print(math.pi) #3.141592653589793


# casting string to number
x = "10001"
y = int(x)
print(type(x)) # <class 'str'>
print(type(y)) # <class 'int'>
print(type(int("New York")))  # Error