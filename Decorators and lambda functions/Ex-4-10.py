#Composition of Decorators: Practice combining multiple decorators.
#Combine simple_logger, timer, and debug_info decorators in different orders on a single function and observe the output differences.
import functools
import time

def simple_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} started")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} ended")
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

def debug_info(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@simple_logger
@timer
@debug_info
def sample_function(x, y):
    time.sleep(1)
    return x + y

print("--- Execution with simple_logger -> timer -> debug_info ---")
print(sample_function(5, 3))

@debug_info
@timer
@simple_logger
def sample_function_reversed(x, y):
    time.sleep(1)
    return x + y

print("\n--- Execution with debug_info -> timer -> simple_logger ---")
print(sample_function_reversed(5, 3))
