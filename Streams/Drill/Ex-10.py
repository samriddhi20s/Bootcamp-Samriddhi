#Advanced Stream Processing: Develop a complex stream processing pipeline that reads from multiple files, filters, processes data, and writes the results to a new file. 
#Include error handling and efficiency considerations.
import itertools

def read_files(file_paths):
    for file_path in file_paths:
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

def write_output(file_path, lines):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line + "\n")
    except IOError:
        print(f"Error: Cannot write to file '{file_path}'.")

def main(input_files, output_file, keyword=None):
    try:
        lines = read_files(input_files)
        filtered_lines = filter_lines(lines, keyword)
        processed_lines = process_lines(filtered_lines)
        write_output(output_file, processed_lines)
        print(f"Processing complete. Results saved in '{output_file}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    input_files = ["file1.txt", "file2.txt"]
    output_file = "output.txt"
    keyword = "filter"
    main(input_files, output_file, keyword)
