#Custom Context Managers: Implement a class that works as a context manager using __enter__ and __exit__ dunder methods.
#Example: A FileOpen class that opens and closes files gracefully.
class FileOpen:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """Open the file and return the file object."""
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """Close the file when the context exits."""
        if self.file:
            self.file.close()
        # handle exceptions (returning True prevents the exception from propagating)
        if exc_type:
            print(f"An error occurred: {exc_value}")
        return False  

# Using the FileOpen context manager
try:
    with FileOpen('example.txt', 'w') as file:
        file.write("Hello, this is a test file.\n")
        print("File has been written successfully.")
except Exception as e:
    print(f"Error during file operation: {e}")
