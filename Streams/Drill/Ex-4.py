#Filtering Data with Iterators: Enhance the file-reading generator to filter out lines that don't meet a certain condition 
#(e.g., lines not containing a specific word).
def filtered_file_generator(filename, keyword):
    """Yields lines from a file that contain the specified keyword."""
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:  
                yield line.strip()  # Remove extra newline characters

# Usage example:
file_path = 'sample.txt' 
keyword = 'error'  # Replace with the keyword you want to filter by

# Use the generator to read and filter the file
for line in filtered_file_generator(file_path, keyword):
    print(line)
