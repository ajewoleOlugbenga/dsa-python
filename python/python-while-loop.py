# Python program to illustrate
# while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
# will start from 0 which is the initial count till any number less than 3

## Python while loop with list

# checks if list still
# contains any element
a = [1, 2, 3, 4]

while a:
    print(a.pop())

#In the above example, we have run a while loop over a list that will run until there is an element present in the list.
#pop() is a method in python to pop out list

##Single statement while block
# Python program to illustrate
# Single statement while block
count = 0
while (count < 5): count += 1; print("Hello Geek")
