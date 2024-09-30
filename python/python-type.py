# type() method returns class type of the argument(object) passed as parameter in Python.

a = ("Geeks", "for", "Geeks")
b = ["Geeks", "for", "Geeks"]
c = {"Geeks": 1, "for": 2, "Geeks": 3}
d = "Hello World"
e = 10.23
f = 11.22

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# type() function is basically used for debugging purposes

##Check object parameter
#In this example, we are testing the object using conditions, and printing the boolean.
print(type([]) is list)
print(type([]) is not list)
print(type(()) is tuple)
print(type(()) is not tuple)
print(type({}) is dict)
print(type({}) is not dict)
