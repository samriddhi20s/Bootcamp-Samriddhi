#Integrating Exception Handling: 
#Enhance the pipeline with exception handling to manage potential errors during file reading or processing.
import itertools

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except IOError:
        print(f"Error: Cannot read file '{file_path}'.")

def filter_lines(lines, keyword=None):
    try:
        for line in lines:
            if line and (keyword is None or keyword not in line):
                yield line
    except Exception as e:
        print(f"Error during filtering: {e}")

def process_lines(lines):
    try:
        for line in lines:
            yield f"{line} (Word count: {len(line.split())})"
    except Exception as e:
        print(f"Error during processing: {e}")

def chain_iterators(*iterables):
    try:
        return itertools.chain(*iterables)
    except Exception as e:
        print(f"Error chaining iterators: {e}")

def main(file_path, keyword=None):
    try:
        lines = read_file(file_path)
        filtered_lines = filter_lines(lines, keyword)
        processed_lines = process_lines(filtered_lines)
        range1, range2 = range(1, 5), range(5, 10)
        combined_ranges = chain_iterators(range1, range2)
        for processed_line in processed_lines:
            print(processed_line)
        print("Combined Ranges:", list(combined_ranges))
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main("sample.txt", "filter")
