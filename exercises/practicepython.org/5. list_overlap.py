a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

## first solution
# mutual_items = {x for x in a for y in b if x == y}

## second solution
# mutual_items = list(set([x for x in a if x in b]))

## Using set intersection to find the common elements in both lists
mutual_items = list(set(a) & set(b))

print(mutual_items)