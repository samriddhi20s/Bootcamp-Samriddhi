#Write a function called str_range(n) that produces n strings in a stream, with "line number {i}" i replaced with the current number.
def str_range(n):
    """Generates a stream of n strings in the format 'line number {i}'."""
    for i in range(1, n + 1):
        yield f"line number {i}"

# Example usage: print the first 20 lines
for line in str_range(20):
    print(line)
