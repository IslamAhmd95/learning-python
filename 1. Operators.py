## Arithmetic Operators

# Addition
print(5 + 3)  # 8

# Subtraction
print(5 - 3)  # 2

# Multiplication
print(5 * 3)  # 15

# Division
print(5 / 3)  # 1.6666666666666667

# Modulus (remainder)
print(5 % 3)  # 2

# Exponentiation (power)
print(5 ** 3)  # 125

# Floor Division (integer division)
print(5 // 3)  # 1

# ----------------------------------------------------------------

## Assignment Operators

# Basic assignment
a = 5
print(a)  # 5

# Add and assign
a += 3  # Equivalent to a = a + 3
print(a)  # 8

# Subtract and assign
a -= 2  # Equivalent to a = a - 2
print(a)  # 6

# Multiply and assign
a *= 2  # Equivalent to a = a * 2
print(a)  # 12

# Divide and assign
a /= 3  # Equivalent to a = a / 3
print(a)  # 4.0

# Modulus and assign
a %= 2  # Equivalent to a = a % 2
print(a)  # 0.0

# Exponentiation and assign
a = 2
a **= 3  # Equivalent to a = a ** 3
print(a)  # 8

# Floor divide and assign
a //= 3  # Equivalent to a = a // 3
print(a)  # 2

# ----------------------------------------------------------------

## Comparison Operators

a = 5
b = 3

# Equal
print(a == b)  # False

# Not equal
print(a != b)  # True

# Greater than
print(a > b)  # True

# Less than
print(a < b)  # False

# Greater than or equal
print(a >= b)  # True

# Less than or equal
print(a <= b)  # False

# --------------------------------------------------------------

## Logical Operators

a = True
b = False

# AND: Returns True if both conditions are True
print(a and b)  # False

# OR: Returns True if at least one condition is True
print(a or b)  # True

# NOT: Inverts the Boolean value
print(not a)  # False

# ----------------------------------------------------------------

## Bitwise Operators

a = 5  # Binary: 101
b = 3  # Binary: 011

# AND: Performs binary AND
print(a & b)  # 1 (Binary: 001)

# OR: Performs binary OR
print(a | b)  # 7 (Binary: 111)

# XOR: Performs binary XOR, The result is 1 if the bits are different and 0 if they are the same.
print(a ^ b)  # 6 (Binary: 110)

# NOT: Inverts the bits
print(~a)  # -6 
# Bitwise NOT is the same as 1's complement (just flipping the bits, 1 becomes 0 and 0 becomes 1). 
# 2's complement is (1's complement + 1).


# Left shift
# What it does: Moves the bits of a number to the left by the specified number of positions.
# Effect: Adds zeros (0) to the right, making the number larger.
# Mathematical Equivalent: Multiplying the number by 2^𝑛, where 𝑛 is the number of positions shifted.
a = 5  # Binary: 101
result = a << 1  # Shift all bits one position to the left: 1010, add a zero (0) to the right: 1010 becomes 10 in decimal.
print(result)    # Output: 10 = 5 * 2^1


# Right shift
# What it does: Moves the bits of a number to the right by the specified number of positions.
# Effect: Removes bits from the right, making the number smaller.
# Mathematical Equivalent: Dividing the number by 2^n, where n is the number of positions shifted, and discarding the remainder (integer division).
a = 20  # Binary: 10100
result = a >> 2  # Shift all bits two positions to the right: 101, drop the last two bits (00 on the far right): 101 becomes 5 in decimal.
print(result)    # Output: 5 = 20 / 2^2

# ----------------------------------------------------------------

## Membership Operators

fruits = ["apple", "banana", "cherry"]

# IN: Returns True if the value is in the sequence
print("apple" in fruits)  # True

# NOT IN: Returns True if the value is NOT in the sequence
print("grape" not in fruits)  # True

# ----------------------------------------------------------------

## Identity Operators

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# IS: Returns True if both variables point to the same object
print(a is b)  # False (different objects with same content)
print(a is c)  # True (same object)

# IS NOT: Returns True if both variables point to different objects
print(a is not b)  # True

# ----------------------------------------------------------------

## Type Operators

print(type(a))  # <class 'list'>
print(type(5))  # <class 'int'>
print(type("hello"))  # <class'str'>

# ----------------------------------------------------------------

## Ternary Operators

x = 5

# Format: value_if_true if condition else value_if_false
result = "Positive" if x > 0 else "Negative"
print(result)  # Positive

