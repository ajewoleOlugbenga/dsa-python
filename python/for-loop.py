#Python For loop is used for sequential traversal i.e.
# it is used for iterating over an iterable like String == "text", Tuple == () , List == [],
# Set == my_set = {1, 2, 3, 4, 5},
# or Dictionary == my_dict = {
#     "name": "John",
#     "age": 30,
#     "job": "Engineer"
# }.

#Using For Loops in Python List
ages = {"Ajewole", "Gbemiga", "Elijah", "Seun"}

for allOfMyName in ages:
    print(allOfMyName, end=" ")
print()

#Using For Loops in Python Dictionary
# Iterating over dictionary
print("Dictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))

#Using For Loops in Python String

print("python string in for loop")

name= "olugbenga"

for g in name:
    print(g, end=" ")