# An attribute (variable)
state = "Kansas"

# A function (method)
def welcome(city):
    print(f"Welcome to {city}, {state}!")

# Another function
def add(a, b):
    return a + b

# Example to demonstrate __name__ and __main__
if __name__ == "__main__":
    print("This code is executed directly in kansas.py")
    print("Running tests for the kansas module:")
    print(f"5 + 3 = {add(5, 3)}")
    welcome("Wichita")
else:
    print("kansas.py module imported elsewhere!")
