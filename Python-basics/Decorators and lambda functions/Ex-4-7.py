#Retry Mechanism Decorator: Implement a decorator to retry a function.
#Develop a retry decorator that retries a function up to a specified number of times if it raises an exception.

import functools
import time

def retry(max_retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    retries += 1
                    print(f"Retry {retries}/{max_retries} for {func.__name__} due to error: {e}")
                    time.sleep(delay)
            print(f"Function {func.__name__} failed after {max_retries} retries.")
            return None
        return wrapper
    return decorator

def role_required(required_role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != required_role:
                print(f"Access denied: {user.get('name')} does not have the required role: {required_role}")
                return None
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

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

@retry(max_retries=3, delay=2)
@role_required("admin")
@debug_info
@memoize
@timer
@prefix_printer("[LOG]")
def unreliable_function(user, n):
    if n % 2 == 0:
        raise ValueError("Even numbers are not allowed!")
    time.sleep(1)
    return n * n

admin_user = {"name": "Alice", "role": "admin"}
regular_user = {"name": "Bob", "role": "user"}

print(unreliable_function(admin_user, 4))
print(unreliable_function(admin_user, 5))
