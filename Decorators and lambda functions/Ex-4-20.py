#Combining functools with List Comprehensions: Integrate functools with list comprehensions.
#Use functools.reduce along with a list comprehension to calculate the sum of squares of numbers from 1 to 10.
import functools

# List comprehension to generate the squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]

# Use functools.reduce to calculate the sum of the squares
sum_of_squares = functools.reduce(lambda a, b: a + b, squares)

# Output the result
print(f"Sum of squares: {sum_of_squares}")
