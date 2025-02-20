from typing import Callable, Iterator
from processing_functions import upper_case, capitalize  

StringFunction = Callable[[str], str]
StreamFunction = Callable[[Iterator[str]], Iterator[str]]

def string_to_stream_function(in_function: StringFunction) -> StreamFunction:
    """Converts a function that processes a single string into a function that processes a stream of strings."""
    def stream_function(input_stream: Iterator[str]) -> Iterator[str]:
        for line in input_stream:
            yield in_function(line)
    return stream_function

stream_upper_case = string_to_stream_function(upper_case)
stream_capitalize = string_to_stream_function(capitalize)

function_lookup = {
    "upper_case": stream_upper_case,
    "capitalize": stream_capitalize,
}
