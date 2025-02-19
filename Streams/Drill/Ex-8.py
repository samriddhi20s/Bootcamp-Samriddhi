#Handling Large Files Efficiently:
#Modify the file processing pipeline to handle large files efficiently without loading the entire file into memory.
import itertools

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

def filter_lines(lines, keyword=None):
    for line in lines:
        if line and (keyword is None or keyword not in line):
            yield line

def process_lines(lines):
    for line in lines:
        yield f"{line} (Word count: {len(line.split())})"

def chain_iterators(*iterables):
    return itertools.chain(*iterables)

def main(file_path, keyword=None):
    lines = read_file(file_path)
    filtered_lines = filter_lines(lines, keyword)
    processed_lines = process_lines(filtered_lines)
    range1, range2 = range(1, 5), range(5, 10)
    combined_ranges = chain_iterators(range1, range2)
    for processed_line in processed_lines:
        print(processed_line)
    print("Combined Ranges:", list(combined_ranges))

if __name__ == "__main__":
    main("sample.txt", "filter")
