import os
from samriddhi_wf_basic.processing_functions import upper_case

def test_upper_case():
    test_input = "test_input.txt"
    test_output = "test_input.txt.processed"

    with open(test_input, "w") as f:
        f.write("hello\nworld")

    upper_case(test_input)

    with open(test_output, "r") as f:
        result = f.read()

    assert result == "HELLO\nWORLD"

    os.remove(test_input)
    os.remove(test_output)
