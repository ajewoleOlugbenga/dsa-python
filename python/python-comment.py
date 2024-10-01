##Python Docstring

# Python docstring is the string literals with triple quotes that are appeared right after the function.
# It is used to associate documentation that has been written with Python modules, functions, classes, and methods.
# It is added right below the functions, modules, or classes to describe what they do.
# In Python, the docstring is then made available via the __doc__ attribute.

def multiply(a, b):
    """Multiplies the value of a and b"""
    return a * b


# Print the docstring of multiply function
print(multiply.__doc__)


def multiply(a, b):
    """Multiplies the value of a and b"""
    return a * b


# Print the docstring of multiply function
print(multiply.__doc__)
