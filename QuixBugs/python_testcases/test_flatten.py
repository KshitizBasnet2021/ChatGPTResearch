import pytest

from QuixBugs.Run_6.flatten import flatten
# from QuixBugs.Run_7.commented_flatten import flatten
from load_testdata import load_json_testcases

# from QuixBugs.correct_python_programs.flatten import flatten
#from QuixBugs.gptTOcode._flatten import flatten

testdata = load_json_testcases(flatten.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_flatten(input_data, expected):
    assert list(flatten(*input_data)) == expected
