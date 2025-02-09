import math


def is_prime(number):
    if number == 1:
        return False
    if number in (2, 3):  # Directly return True for 2 and 3
        return True
    if number % 2 == 0 or number % 3 == 0:  # Eliminate multiples of 2 and 3 early
        return False
    return all(number % i != 0 for i in range(5, math.isqrt(number)+1, 2))


while True:
    try:
        number = int(input("Enter the number: ").strip())
        if number < 0:
            print("Negative number is not allowed.\n")
            continue
        break  # Exit the loop when a valid number is entered
    except ValueError:
        print("Invalid input. Please enter a valid integer.\n")


if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")