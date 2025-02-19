#List Comprehension with Multiple Iterables: Use multiple iterables in a list comprehension.
#Generate all possible pairs (as tuples) of numbers from two different lists using a list comprehension.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

pairs = [(x, y) for x in list1 for y in list2]
print(pairs)
