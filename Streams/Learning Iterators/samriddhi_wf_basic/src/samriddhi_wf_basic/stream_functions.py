from typing import Iterator

def number_the_lines(lines: Iterator[str]) -> Iterator[str]:
    """Add line numbers as a prefix to each line."""
    for i, line in enumerate(lines, 1):
        yield f"{i}: {line}"

def coalesce_empty_lines(lines: Iterator[str]) -> Iterator[str]:
    """Remove multiple empty lines, keeping only one."""
    previous_was_empty = False
    for line in lines:
        if line.strip():
            yield line
            previous_was_empty = False
        elif not previous_was_empty:
            yield line
            previous_was_empty = True

def remove_empty_lines(lines: Iterator[str]) -> Iterator[str]:
    """Remove all empty lines."""
    for line in lines:
        if line.strip():
            yield line

def remove_even_lines(lines: Iterator[str]) -> Iterator[str]:
    """Remove all even-numbered lines."""
    for i, line in enumerate(lines, 1):
        if i % 2 != 0:
            yield line

def break_lines(lines: Iterator[str], length: int = 20) -> Iterator[str]:
    """Break long lines into smaller segments."""
    for line in lines:
        for i in range(0, len(line), length):
            yield line[i:i + length]
