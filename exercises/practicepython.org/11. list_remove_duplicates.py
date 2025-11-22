import random


def remove_duplicates(input_list):
    return set(input_list)

# def remove_duplicates(input_list):
#     unique_list = []
#     seen = set()

#     for item in input_list:
#         if item not in seen:
#             unique_list.append(item)
#             seen.add(item)

#     return unique_list

original_list = random.choices(range(15), k=10)
print("Original list:", original_list)

no_duplicates_list = remove_duplicates(original_list)
print("List without duplicates:", list(no_duplicates_list))