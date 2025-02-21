#Basic Function Decorator: Learn to write a basic decorator for a function.
#Create a decorator named simple_logger that prints "Function started" and "Function ended" when any function is called.

import functools

def simple_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

@simple_logger
def say_hello():
    print("Hello, world!")

say_hello()
