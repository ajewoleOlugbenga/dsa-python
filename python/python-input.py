##Two input option to provide data
# 1.input
# 2. raw_input

val = input("Enter a value: \n")
print("The value you entered is: " + val)

# raw_input(): This function works in older version (like Python 2.x).
# This function takes exactly what is typed from the keyboard, converts it to string,
# and then returns it to the variable in which we want to store it.

# Python program showing
# a use of raw_input()

#g = raw_input("Enter your name : ")
#print g

# Python program to take integer input  in Python

# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map, split and strip functions
lst = list(map(int, input(
    "Enter the integer elements of list(Space-Separated): ").strip().split()))[:n]
print('The list is:', lst)  # printing the list

