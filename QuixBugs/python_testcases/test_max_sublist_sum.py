import pytest
from load_testdata import load_json_testcases

from QuixBugs.correct_python_programs.max_sublist_sum import max_sublist_sum
#from QuixBugs.gptTOcode._max_sublist_sum import max_sublist_sum

testdata = load_json_testcases(max_sublist_sum.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_max_sublist_sum(input_data, expected):
    assert max_sublist_sum(*input_data) == expected
