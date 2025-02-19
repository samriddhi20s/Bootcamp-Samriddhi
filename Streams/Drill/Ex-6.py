#File Processing Pipeline: Create a pipeline that reads from a file, filters lines, and then processes them 
#(e.g., count the number of words in each line).
def read_file(file_path):
    """Reads a file line by line."""
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def filter_lines(lines, keyword=None):
    """Filters out empty lines and optionally lines containing a keyword."""
    for line in lines:
        if line and (keyword is None or keyword not in line):
            yield line


def process_lines(lines):
    """Processes lines by counting the number of words in each line."""
    for line in lines:
        word_count = len(line.split())
        yield f"{line} (Word count: {word_count})"


def main(file_path, keyword=None):
    lines = read_file(file_path)
    filtered_lines = filter_lines(lines, keyword)
    processed_lines = process_lines(filtered_lines)
    
    for processed_line in processed_lines:
        print(processed_line)


if __name__ == "__main__":
    file_path = "sample.txt"  
    keyword = "filter"  # Change this to filter specific words (or set to None)
    main(file_path, keyword)
