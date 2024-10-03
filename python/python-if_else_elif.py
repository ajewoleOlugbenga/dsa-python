# if statement example
if 10 > 5:
    print("10 is greater than 5")

print("Program ended")

# if..else statement example

x=3
if x==4:
    print("Yes")
else:
    print("No")

# You can also chain if..else statement with more than one condition.
# if..else chain statement
letter = "A"

if letter == "B":
    print("letter is B")

else:

    if letter == "C":
        print("letter is C")

    else:

        if letter == "A":
            print("letter is A")

        else:
            print("letter isn't A, B and C")

## Nested if Statement
# if statement can also be checked inside other if statement.
# This conditional statement is called a nested if statement.
# This means that inner if condition will be checked only if outer if condition is true and by this,
# we can see multiple conditions to be satisfied.

# Nested if statement example
num = 10

if num > 5:
    print("Bigger than 5")

    if num <= 15:
        print("Between 5 and 15")


# if-elif Statement

# if-elif statement example

letter = int(2)

if letter == "B":
    print("letter is B")

elif letter == "C":
    print("letter is C")

elif letter == "A":
    print("letter is A")

elif isinstance(letter, int):
    print("letter is an integer")

else:
    print("letter isn't A, B or C")


def checking(a, b):
    """isinstance- is used to check if a value is of the-same data type"""
    return a + b


print(checking.__doc__)

print(1//2 + 1.0/2)

