#Write a program that uses this function that skips the first 10 and then prints the 10 next fibonacci numbers and exits.
from itertools import islice

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Skip first 10 Fibonacci numbers and print the next 10
fib_gen = fibonacci()
for num in islice(fib_gen, 10, 20):
    print(num)
