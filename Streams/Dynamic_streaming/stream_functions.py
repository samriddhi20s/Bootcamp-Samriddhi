from typing import Iterator

def coalesce_empty_lines(input_stream: Iterator[str]) -> Iterator[str]:
    """Replaces multiple empty lines with a single empty line."""
    prev_was_empty = False
    for line in input_stream:
        if line.strip():
            yield line
            prev_was_empty = False
        elif not prev_was_empty:
            yield line
            prev_was_empty = True

def break_lines(input_stream: Iterator[str]) -> Iterator[str]:
    """Breaks long lines into chunks of 20 characters."""
    for line in input_stream:
        for i in range(0, len(line), 20):
            yield line[i:i+20]

def number_the_lines(input_stream: Iterator[str]) -> Iterator[str]:
    """Prefixes lines with line numbers."""
    for i, line in enumerate(input_stream, start=1):
        yield f"{i} {line}"
