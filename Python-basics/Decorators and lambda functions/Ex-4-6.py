#Access Control Decorator: Write a decorator to restrict access to a function.
#Create a role_required decorator that takes a user role and only allows the function to execute if the provided user has the specified role.
import functools
import time

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

@role_required("admin")
@debug_info
@memoize
@timer
@prefix_printer("[LOG]")
def restricted_function(user, n):
    time.sleep(1)
    return n * n

admin_user = {"name": "Alice", "role": "admin"}
regular_user = {"name": "Bob", "role": "user"}

print(restricted_function(admin_user, 4))
print(restricted_function(regular_user, 4))
