def add_one(num, total=0):
    total += num
    if total >= 9:
        return total+1
    print(total)
    return add_one(1, total)  # When a recursive call is made, the result of the inner call (add_one(1, total)) needs to be returned to the caller function so the chain of recursion can propagate the final result back to the original call, Without return, the result of the recursive call would be computed but not returned, and the calling function would not receive the correct value.

newTotal = add_one(0)
print(newTotal)


# When to Use return:
    # To pass a result back to the caller, whether it’s the same function (recursion) or another function.
# When Not to Use return:
    # If you’re calling a function just to perform an action (like printing or logging), and you don’t need any result from it.

def calculate_factorial(num):
    if num <= 1:
        return 1
    else:
        return num * calculate_factorial(num - 1) # 5 * 4 * 3 * 2 * 1
    
num = int(input('Enter a number: '))
print(calculate_factorial(num))


def make_word(charlist):
    # The recursive function requires a stopping condition (base case) to avoid infinite recursion or an eventual error when the input becomes invalid (like accessing an index out of range).
    if len(charlist) == 0:    # the stopping condition or the base case
        return '.'
    else:
    #     return charlist.pop(0) + make_word(charlist)
        return charlist[0] + make_word(charlist[1:])


charlist = ['T', 'h', 'a', 'n', 'k', ' ', 'y', 'o', 'u']
print(make_word(charlist))