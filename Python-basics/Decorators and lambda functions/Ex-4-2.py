#Decorator with Arguments: Create a decorator that can take arguments.
#Write a decorator named prefix_printer that takes a string prefix and prints it before the function's name each time the function is called.
import functools

def prefix_printer(prefix):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix} {func.__name__} started")
            result = func(*args, **kwargs)
            print(f"{prefix} {func.__name__} ended")
            return result
        return wrapper
    return decorator

@prefix_printer("[LOG]")
def say_hello():
    print("Hello, world!")

say_hello()
