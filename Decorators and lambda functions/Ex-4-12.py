#Conditional List Comprehension: Use a condition within a list comprehension.
#Create a list of even numbers from 1 to 20 using a list comprehension with a conditional statement.
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)
