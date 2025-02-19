#Custom Iterator for File Reading: Write a custom iterator that reads a file line by line. 
#Test this by reading a sample text file and printing each line.
class FileIterator:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')  # Open the file in read mode
        self.line = None

    def __iter__(self):
        return self

    def __next__(self):
        self.line = self.file.readline()
        if not self.line:  # If we reach the end of the file
            self.file.close()  # Close the file when done
            raise StopIteration
        return self.line.strip()  # Remove any extra newline characters

# Usage example:
file_path = 'sample.txt'  # Replace with the path to your sample text file

# Create an instance of the iterator
file_iterator = FileIterator(file_path)

# Use the iterator in a for loop to print each line
for line in file_iterator:
    print(line)
