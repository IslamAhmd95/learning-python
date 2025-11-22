def fibonacci(n):
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    sequence = [0, 1]  # Start with the first two Fibonacci numbers
    for _ in range( n - 2):  # Generate the remaining numbers
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence

try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Input must be a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()


print(*fibonacci(n))  # Using * to unpack the list into separate arguments


#----------------------------------------------------------------

# another solution

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Input must be a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

fibonacci(n)

