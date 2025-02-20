#Write a function that takes a file name and produces a stream of records. Hint: You can use fileinput module.
import fileinput

def file_stream(filename):
    """Generates a stream of lines from a file."""
    with fileinput.input(files=filename) as f:
        for line in f:
            yield line.strip()  # Yield each line without trailing newline


if __name__ == "__main__":
    filename = "example.txt"  # Replace with your actual file name
    for record in file_stream(filename):
        print(record)
