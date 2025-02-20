import sys
from stream_functions import coalesce_empty_lines, break_lines, number_the_lines
from stream_adapter_function import function_lookup
from typing import Iterator


pipeline = [
    coalesce_empty_lines,
    break_lines,
    number_the_lines,
    function_lookup["capitalize"],  
]

def process_pipeline(input_stream: Iterator[str], pipeline: list) -> Iterator[str]:
    """Processes input through a series of streaming functions."""
    for function in pipeline:
        input_stream = function(input_stream)
    return input_stream

if __name__ == "__main__":
    input_stream = (line.rstrip("\n") for line in sys.stdin)  # Read from stdin
    output_stream = process_pipeline(input_stream, pipeline)
    for line in output_stream:
        print(line)  
