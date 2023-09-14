import pytest
from load_testdata import load_json_testcases

# from QuixBugs.python_programs.pascal import pascal
from QuixBugs.gptTOcode._pascal import pascal

testdata = load_json_testcases(pascal.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_pascal(input_data, expected):
    assert pascal(*input_data) == expected
