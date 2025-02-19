#Timing Decorator: Implement a decorator to measure execution time.
#Develop a timer decorator that prints the time taken by a function to execute.
import functools
import time

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

@timer
@prefix_printer("[LOG]")
def say_hello():
    print("Hello, world!")
    time.sleep(1)  # Simulating a delay

say_hello()
