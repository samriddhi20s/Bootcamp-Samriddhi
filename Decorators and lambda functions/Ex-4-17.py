#functools.lru_cache for Optimization: Optimize a recursive function with lru_cache.
#Write a recursive function to calculate Fibonacci numbers and use functools.lru_cache to optimize it.
import functools

# Define the Fibonacci function with LRU cache
@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
n = 10
print(f"Fibonacci number at position {n}: {fibonacci(n)}")
