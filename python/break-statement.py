#Python break is used to terminate the execution of the loop.

# Syntax:
#
# Loop{
#     Condition:
#         break
#     }

for i in range(10):
    print(i, end=" ")
    if i==2:
        break


myNames = "Ajewole Olugbenga Elijah"

for allMyNames in myNames:
    print(allMyNames, end=" ")
    if allMyNames == "E":
        break
print("out of loop"   )
print()


num = 0
for i in range(10):
    num +=1
    if i == 8:
        break
    print("the next number is: ", num)
print("out of loop")
