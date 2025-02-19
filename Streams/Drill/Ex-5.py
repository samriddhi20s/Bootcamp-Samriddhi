#Creating a Stream Processing Function: Write a function that takes an iterator as input and processes its items,
#e.g., multiplying numbers by 2. Test this with a range iterator.
def process_stream(iterator):
    for item in iterator:
        yield item * 2

# Test with a range iterator
numbers = range(1, 6)  
processed_numbers = process_stream(numbers)

for num in processed_numbers:
    print(num)
