#Syntax: range(start, stop, step)
#Parameter:
#start: [ optional ] start value of the sequence
#stop: next value after the end value of the sequence
#step: [ optional ] integer value, denoting the difference between any two numbers in the sequence.
#Return: Returns a range type object.
from random import random

# print first 5 integers
# using python range() function
for i in range(5):
    print(i, end=" ")
print()

#print first 6 integers
for i in range(6):
    print(i, end=" ")
print()

#note the only compulsory argument in range is stop

#Python range() function takes can be initialized in 3 ways.
#range (stop) takes one argument.
#range (start, stop) takes two arguments.
#range (start, stop, step) takes three arguments.

#range(stop)
#When the user call range() with one argument,
# the user will get a series of numbers that starts at 0 and includes every whole number up to,
# but not including, the number that the user has provided as the stop.

for u in range(9):
    print(u, end=" ")
print()

##range(start, stop)

#When the user call range() with two arguments,
# the user gets to decide not only where the series of numbers stops but also where it starts,
# so the user don’t have to start at 0 all the time.
# Users can use range() to generate a series of numbers from X to Y using range(X, Y).

for y in range(10, 30):
    print(y, end=" ")
print()

##range(start, stop, step)
#When the user call range() with three arguments,
# the user can choose not only where the series of numbers will start and stop,
# but also how big the difference will be between one number and the next.
# If the user doesn’t provide a step, then range() will automatically behave as if the step is 1.
# In this example,
# we are printing even numbers between 0 and 10, so we choose our starting point from 0(start = 0) and stop the series at 10(stop = 10).
# For printing an even number the difference between one number and the next must be 2 (step = 2) after providing a step we get the following output (0, 2, 4, 8).

#range(start, stop, step)
for ages in range(20,80,5):
    print(ages, end=" ")
print()