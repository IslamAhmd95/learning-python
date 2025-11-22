
def even_or_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even"
    return f"The number {number} is odd"

def multiple_of_four(number):
    if number % 4 == 0:
        return f"The number {number} is a multiple of 4"
    return f"The number {number} is not a multiple of 4"

def divide_by_check(number, check_number): 
    if number % check_number == 0:
        return f"The number {number} is evenly divisible by {check_number}"
    return f"The number {number} is not evenly divisible by {check_number}"


try:
    number = int(input("Enter a number to check: ").strip())
    check_number = int(input("Enter a number to divide by: ").strip())
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()


print(even_or_odd(number))
print(multiple_of_four(number))
print(divide_by_check(number, check_number))
