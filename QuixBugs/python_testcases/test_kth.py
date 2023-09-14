import pytest
from load_testdata import load_json_testcases

# from QuixBugs.python_programs.kth import kth
from QuixBugs.gptTOcode._kth import kth

testdata = load_json_testcases(kth.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kth(input_data, expected):
    assert kth(*input_data) == expected
