#Basic Iterator Creation: Create a simple iterator that yields numbers from 1 to 10. 
#Use a for loop to iterate over this iterator and print the numbers.
class NumberIterator:
    def __init__(self):
        self.current = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 10:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

# Using the iterator
iterator = NumberIterator()

for number in iterator:
    print(number)
