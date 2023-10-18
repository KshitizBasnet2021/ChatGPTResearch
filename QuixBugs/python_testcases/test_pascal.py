import pytest

# from QuixBugs.Run_6.pascal import pascal
from QuixBugs.Run_7.commented_pascal import pascal
from load_testdata import load_json_testcases

# from QuixBugs.correct_python_programs.pascal import pascal
#from QuixBugs.gptTOcode._pascal import pascal

testdata = load_json_testcases(pascal.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_pascal(input_data, expected):
    assert pascal(*input_data) == expected
