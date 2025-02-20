#Write a function called str_range(n) that produces n strings in a stream, with "line number {i}" i replaced with the current number.
def str_range(n):
    """Generates a stream of n strings in the format 'line number {i}'."""
    for i in range(1, n + 1):
        yield f"line number {i}"

for line in str_range(10):
    print(line)
