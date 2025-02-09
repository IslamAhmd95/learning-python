person = "islam"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left")

message = "\n%s has %s coins left" %(person, coins)
print(message)

message ="\n{} has {} coins left".format(person, coins)
print(message)

message ="\n{person} has {coins} coins left".format(person=person, coins=coins)
print(message)

message ="\n{1} has {0} coins left".format(coins, person)  # using index way
print(message)

player = {"person": "islam", "coins": coins}
message ="\n{person} has {coins} coins left".format(**player)
print(message)

#----------------------------------------------------------------

# f-strings
message = f"\n{person} has {coins} coins left"
print(message)

message = f"\n{person.capitalize()} has {2 * 5} coins left"
print(message)

message = f"\n{player['person'].capitalize()} has {5} coins left"
print(message)

# pass formatting options
num = 10
message = f"2.2352 times of num equals {2.2352 * num:.2f}"
print(message)  # 2.2352 times of num equals 22.35
# :.2f tells Python to format the number with two decimal places.
# The number 22.352 is rounded to 22.35 when printed.

#----------------------------------------------------------------

## string format

# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.
# The format() method returns the formatted string.

# Formatting types in Python:

# 1. Alignments
# ------------- 
# :<    Left-align the content
# :>    Right-align the content
# :^    Center-align the content

text = "Hello"
print(f"{text:<10}")  # Left-align, width of 10
print(f"{text:>10}")  # Right-align, width of 10
print(f"{text:^10}")  # Center-align, width of 10

# Output:
# Hello     
#      Hello
#   Hello   

# 2. Width and Fill
# -----------------
# You can specify a fill character before the alignment symbol.
# The default fill is a space.

print(f"{text:_<10}")  # Fill with underscores, left-align
print(f"{text:*>10}")  # Fill with asterisks, right-align
print(f"{text:#^10}")  # Fill with hashes, center-align

# Output:
# Hello_____
# *****Hello
# ##Hello###

# 3. Numbers with Alignment
# -------------------------
# Numbers can also be aligned in a specific width.

number = 123
print(f"{number:<10}")  # Left-align
print(f"{number:>10}")  # Right-align
print(f"{number:^10}")  # Center-align

# Output:
# 123       
#        123
#    123    

# 4. Formatting Numbers
# ---------------------
# :,    Add commas as thousands separators
# .nf   Set the number of decimal places
# %     Display as a percentage
# e     Scientific notation

number = 1234567.8912
print(f"{number:,}")      # Add commas
print(f"{number:.2f}")    # Two decimal places
print(f"{number:.0f}")    # No decimal places
print(f"{number:.2%}")    # Percentage
print(f"{number:.2e}")    # Scientific notation

# Output:
# 1,234,567.8912
# 1234567.89
# 1234568
# 123456789.12%
# 1.23e+06

# 5. Combining Width, Fill, and Numbers
# -------------------------------------
print(f"{number:*>15,.2f}")  # Right-align, asterisks as fill, commas, and 2 decimal places
print(f"{number:_^20,.2f}")  # Center-align, underscores as fill, commas, and 2 decimal places

# Output:
# *****1,234,567.89
# ___1,234,567.89___

# 6. Binary, Octal, Hexadecimal
# -----------------------------
# b     Binary representation
# o     Octal representation
# x     Hexadecimal (lowercase)
# X     Hexadecimal (uppercase)

number = 255
print(f"{number:b}")  # Binary
print(f"{number:o}")  # Octal
print(f"{number:x}")  # Hexadecimal (lowercase)
print(f"{number:X}")  # Hexadecimal (uppercase)

# Output:
# 11111111
# 377
# ff
# FF

# 7. String Truncation
# --------------------
# .n   Limit the length of the string to n characters.

text = "Hello, World!"
print(f"{text:.5}")  # Only the first 5 characters

# Output:
# Hello

# 8. Sign Formatting
# ------------------
# +     Show sign for both positive and negative numbers
# -     Show sign only for negative numbers (default)
# space Leave a leading space for positive numbers

number = 42
print(f"{number:+}")    # Show positive sign
print(f"{number:-}")    # Default (negative only)
print(f"{number: }")    # Leave a space for positive numbers

# Output:
# +42
# 42
#  42

# 9. Customizing Percentage
# -------------------------
percentage = 0.25678
print(f"{percentage:.2%}")  # 2 decimal places, percentage format
print(f"{percentage:>10.2%}")  # Right-align the percentage, width of 10

# Output:
# 25.68%
#    25.68%
