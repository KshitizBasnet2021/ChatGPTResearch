import pytest

from QuixBugs.Run_6.next_palindrome import next_palindrome
from load_testdata import load_json_testcases

# from QuixBugs.correct_python_programs.next_palindrome import next_palindrome
#from QuixBugs.gptTOcode._next_palindrome import next_palindrome

testdata = load_json_testcases(next_palindrome.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_next_palindrome(input_data, expected):
    assert next_palindrome(*input_data) == expected
