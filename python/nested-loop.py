##Nested loops mean loops inside a loop.
#For example, while loop inside the for loop, for loop inside the for loop, etc.

##Python Nested Loops Syntax:
# Outer_loop Expression:

# Inner_loop Expression:

# Statement
# inside
# inner_loop
#
# Statement
# inside
# Outer_loop

x = [1, 2]
y = [4, 5]

for i in x:
    for j in y:
        print(i, j)
print("\n")

for i in range(2, 4):
    for j in range(1, 11):
        print(i, "*", j, "=", i*j)
    print()

# Initialize list1 and list2
# with some strings
list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'geek']

# Store length of list2 in list2_size
list2_size = len(list2)

# Running outer for loop to
# iterate through a list1.
for item in list1:

    # Printing outside inner loop
    print("start outer for loop ")
    # Initialize counter i with 0
    i = 0
    # Running inner While loop to
    # iterate through a list2.
    while (i < list2_size):
        # Printing inside inner loop
        print(item, list2[i])
        # Incrementing the value of i
        i = i + 1
    # Printing outside inner loop
    print("end for loop ")
