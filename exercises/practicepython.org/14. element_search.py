

# def check_number(number, list_to_check, original_list):
    
#     if not list_to_check:
#         return f"Number {number} does not exist in the list."

#     mid_index = len(list_to_check) // 2
#     mid_item = list_to_check[mid_index]

#     if mid_item == number:
#         return f"Number {number} exists in the list with index {original_list.index(number)}"
#     elif number < mid_item:
#         return check_number(number, list_to_check[:mid_index], original_list)  # first half
#     elif number > mid_item:
#         return check_number(number, list_to_check[mid_index + 1:], original_list)  # second half

def binary_search(number, list_to_check):
    
    left, right = 0, len(list_to_check) - 1

    while left <= right:

        mid_index = (left + right) // 2
        mid_item = list_to_check[mid_index]

        if number == mid_item:
            return f"Number {number} exists in the list with index {mid_index}"
        elif number < mid_item:
            right = mid_index - 1
        else:
            left = mid_index + 1
        
    return f"Number {number} does not exist in the list."


a = [30, 5, 42, 1, 43, 3, 500, 42]

try:
    user_number = int(input("\nEnter a number: ").strip())
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

a_sorted_no_duplicates = list(dict.fromkeys(sorted(a)))
print(a_sorted_no_duplicates)
print(binary_search(user_number, a_sorted_no_duplicates))