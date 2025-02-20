#Write a program that uses this str_range to iterate over the first 20 strings to print them out.
def str_range(n):
    """Generates a stream of n strings in the format 'line number {i}'."""
    for i in range(1, n + 1):
        yield f"line number {i}"

# Program to print the first 20 lines
def print_str_range():
    for line in str_range(20):
        print(line)

if __name__ == "__main__":
    print_str_range()
