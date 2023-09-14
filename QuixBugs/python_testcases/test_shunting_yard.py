import pytest
from load_testdata import load_json_testcases

# from QuixBugs.python_programs.shunting_yard import shunting_yard
from QuixBugs.gptTOcode._shunting_yard import shunting_yard

testdata = load_json_testcases(shunting_yard.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_shunting_yard(input_data, expected):
    assert shunting_yard(*input_data) == expected
