## While loop

value = 1
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Current value is " + str(value))

# The else block in a while loop executes only when the loop terminates normally (i.e., when the loop condition becomes False). If the loop is terminated prematurely "قبل الأوان" using a break statement, the else block is skipped. it's only exists in python .


# For loop

for x in "islam":
    if "islam".index(x) == 0: # skip first character
        continue
    elif "islam".index(x) == len("islam")-1: # skip last character
        break
    print(x)

for x in range(2, 4):
    print(x)  # 2, 3


for x in range(5, 101, 5):
    print(x)  # 5, 10, 15, ..., 100
    # if x == 95:
    #     break   # in this case, the else statement will not be executed
else:
    print("Glad that this over now!") # runs after the loop ends unless the break statement is used 