import pytest
from load_testdata import load_json_testcases

# from QuixBugs.python_programs.possible_change import possible_change
from QuixBugs.gptTOcode._possible_change import possible_change

testdata = load_json_testcases(possible_change.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_possible_change(input_data, expected):
    assert possible_change(*input_data) == expected
