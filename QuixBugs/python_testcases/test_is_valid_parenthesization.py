import pytest

# from QuixBugs.Run_6.is_valid_parenthesization import is_valid_parenthesization
from QuixBugs.Run_7.commented_is_valid_parenthesization import is_valid_parenthesization
from load_testdata import load_json_testcases

# from QuixBugs.correct_python_programs.is_valid_parenthesization import is_valid_parenthesization
#from QuixBugs.gptTOcode._is_valid_parenthesization import is_valid_parenthesization

testdata = load_json_testcases(is_valid_parenthesization.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_is_valid_parenthesization(input_data, expected):
    assert is_valid_parenthesization(*input_data) == expected
