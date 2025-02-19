#Combining functools.reduce with Lambda: Implement reduce with a lambda function.
#Utilize functools.reduce and a lambda function to calculate the factorial of a number.
from functools import reduce

# Factorial using reduce and lambda
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))

print(factorial(5))  # Output: 120
print(factorial(7))  # Output: 5040
