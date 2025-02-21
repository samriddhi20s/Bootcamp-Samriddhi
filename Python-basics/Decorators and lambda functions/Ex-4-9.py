#Class Method Decorator: Apply a decorator to class methods.
#Implement a validate_args decorator that checks and validates the arguments passed to any class method in which it is used.
import functools
import time

def validate_args(validator):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if not validator(*args, **kwargs):
                raise ValueError(f"Invalid arguments passed to {func.__name__}")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator

def custom_logger(log_message):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{log_message} - Starting {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{log_message} - Finished {func.__name__}")
            return result
        return wrapper
    return decorator

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

class Calculator:
    @validate_args(lambda x, y: isinstance(x, (int, float)) and isinstance(y, (int, float)))
    @custom_logger("Performing Calculation")
    @timer
    def add(self, x, y):
        return x + y

calculator = Calculator()
print(calculator.add(5, 3))
