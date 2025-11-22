def check_items(item, check_number):
    return item < check_number
    
try:
    check_number = int(input("Enter number for check: ").strip())
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

original_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

"""
The filter() function in Python expects the function (or lambda) passed to it to return a boolean value (True or False).
    If the function returns True, the element is included in the filtered result.
    If the function returns False, the element is excluded from the filtered result.

 Why the Filter Function Must Return True or False:
    filter() works by iterating over each element of the list and applying the given function (in your case, the lambda or check_items()). If the function returns True for an element, that element will be kept; if it returns False, the element will be discarded.
"""
new_list = list(filter(lambda item: check_items(item, check_number), original_list))

## another solution without function

# new_list = list(filter(lambda item: item < check_number, original_list))

## another solution with list comprehension

# new_list = [item for item in original_list if item < check_number]

print(new_list)