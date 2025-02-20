from samriddhi_wf_basic.stream_functions import *

def test_number_the_lines():
    lines = iter(["Hello", "World"])
    result = list(number_the_lines(lines))
    assert result == ["1: Hello", "2: World"]

def test_coalesce_empty_lines():
    lines = iter(["Hello", "", "", "World", ""])
    result = list(coalesce_empty_lines(lines))
    assert result == ["Hello", "", "World", ""]

def test_remove_empty_lines():
    lines = iter(["Hello", "", "World", "", ""])
    result = list(remove_empty_lines(lines))
    assert result == ["Hello", "World"]

def test_remove_even_lines():
    lines = iter(["Line1", "Line2", "Line3", "Line4", "Line5"])
    result = list(remove_even_lines(lines))
    assert result == ["Line1", "Line3", "Line5"]

def test_break_lines():
    lines = iter(["This is a long line that should be broken."])
    result = list(break_lines(lines, length=10))
    assert result == ["This is a ", "long line ", "that shoul", "d be broke", "n."]
