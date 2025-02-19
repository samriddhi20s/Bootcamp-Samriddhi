#Debug Information Decorator: Build a decorator to print function details.
#Implement a debug_info decorator that prints the name of the function, its arguments, and its return value each time the function is called.

import functools
import time

def debug_info(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

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

@debug_info
@memoize
@timer
@prefix_printer("[LOG]")
def slow_function(n):
    time.sleep(1)
    return n * n

print(slow_function(4))
print(slow_function(4))
