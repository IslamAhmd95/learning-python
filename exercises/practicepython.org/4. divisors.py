import math

try:
    number = int(input("Enter a number: ").strip())

    if number < 0:
        print("Error: Negative numbers are not allowed")
        exit()

except ValueError as e:
    print("Please enter a valid integer")
    exit()

divisors = set()
for i in range(1, math.isqrt(number) + 1):
    """
    Any number greater than √number does not need to be checked.
        Every divisor less than or equal to √N has a corresponding divisor greater than √N.
        Once we find i as a divisor, we automatically get N // i as another divisor.
        So, we only need to check up to √N, because the second half of divisors will already be covered.
    """
    if number % i == 0:
        divisors.add(i)
        if i * i!= number:
            divisors.add(number // i)

print(f"The divisors of number {number} is {sorted(divisors)}")

"""
Why math.isqrt(N)?
    Instead of math.sqrt(N), we use math.isqrt(N) because:
        It gives an integer result (e.g., math.isqrt(100) = 10).
        No floating-point rounding issues.
        We can use it directly in a loop.
        num = 10
        print(math.sqrt(num))   # Output: 3.1622776601683795 (float)
        print(math.isqrt(num))  # Output: 3 (int)
"""