import pytest
from load_testdata import load_json_testcases

# from QuixBugs.python_programs.rpn_eval import rpn_eval
from QuixBugs.gptTOcode._rpn_eval import rpn_eval

testdata = load_json_testcases(rpn_eval.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_rpn_eval(input_data, expected):
    assert rpn_eval(*input_data) == expected
