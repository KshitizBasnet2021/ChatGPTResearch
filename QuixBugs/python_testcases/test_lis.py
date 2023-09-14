import pytest
from load_testdata import load_json_testcases

# from QuixBugs.python_programs.lis import lis
from QuixBugs.gptTOcode._lis import lis

testdata = load_json_testcases(lis.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_lis(input_data, expected):
    assert lis(*input_data) == expected
