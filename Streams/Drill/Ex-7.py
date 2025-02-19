#Chaining Iterators: Utilize itertools.chain to combine multiple iterators into one. 
#Create a combined iterator from several range objects and process them.
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
        word_count = len(line.split())
        yield f"{line} (Word count: {word_count})"


def chain_iterators(*iterables):
    return itertools.chain(*iterables)


def main(file_path, keyword=None):
    lines = read_file(file_path)
    filtered_lines = filter_lines(lines, keyword)
    processed_lines = process_lines(filtered_lines)
    
    range1 = range(1, 5)
    range2 = range(5, 10)
    combined_ranges = chain_iterators(range1, range2)
    
    for processed_line in processed_lines:
        print(processed_line)
    
    print("Combined Ranges:", list(combined_ranges))


if __name__ == "__main__":
    file_path = "sample.txt" 
    keyword = "filter" 
    main(file_path, keyword)
