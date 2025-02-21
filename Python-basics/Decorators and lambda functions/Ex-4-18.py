#Advanced List Comprehension: Implement more complex logic in a list comprehension.
#Create a list comprehension that transforms all strings in a list to uppercase and all integers to their square values.

input_list = ["hello", 3, "world", 5, "python", 2]

# List comprehension with conditional logic
output_list = [item.upper() if isinstance(item, str) else item**2 if isinstance(item, int) else item for item in input_list]

# the transformed list
print(output_list)
