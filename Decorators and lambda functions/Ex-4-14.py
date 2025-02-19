#functools.partial Usage: Learn to use partial from the functools module.
#Use functools.partial to create a new function that multiplies any number by 2, based on a generic multiplication function.
from functools import partial

def multiply(x, y):
    return x * y

# Create a new function that always multiplies by 2
double = partial(multiply, 2)

print(double(5))  # Output: 10
print(double(10)) # Output: 20
