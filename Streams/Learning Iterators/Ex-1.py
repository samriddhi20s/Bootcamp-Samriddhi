#Write a function called fibonacci that keeps on producing all fibonacci numbers -- an infinite sequence.
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
from fibonacci import fibonacci

def print_fibonacci():
    fib_gen = fibonacci()
    for num in islice(fib_gen, 10, 20):
        print(num)

if __name__ == "__main__":
    print_fibonacci()
