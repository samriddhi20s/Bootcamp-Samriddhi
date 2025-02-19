#Nested List Comprehension: Explore nested list comprehensions.
#Use a nested list comprehension to flatten a matrix (a list of lists) into a single list.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)
