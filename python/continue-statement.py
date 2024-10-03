## continue inside some condition within a loop

for names in "Olugbenga":
    if names == "n":
        continue
    print(names, end=" ")
print("\n")
#Here we are skipping the print of character ‘n’ using if-condition checking and continue statement.


#loop from 1 to 10 my way
num = 0

for num in range(10):
    num+=1
    if num == 6 or num == 8:
        continue
    print(num, end=" ")



# loop from 1 to 10 geeksforgeeks way
for i in range(1, 11):

    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")
