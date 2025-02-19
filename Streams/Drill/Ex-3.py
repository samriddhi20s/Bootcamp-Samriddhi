#Using Generators: Convert the custom file reading iterator into a generator that yields lines from a file. 
#Demonstrate its usage with a sample file.
def file_generator(filename):
    with open(filename, 'r') as file:  # Open the file using a context manager
        for line in file:
            yield line.strip()  # Yield each line without newline characters

# Usage example:
file_path = 'sample.txt'  # Replace with your actual file path

# Use the generator to read the file line by line
for line in file_generator(file_path):
    print(line)
