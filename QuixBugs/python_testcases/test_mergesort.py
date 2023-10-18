import pytest
from load_testdata import load_json_testcases

# from QuixBugs.python_programs.mergesort import mergesort
from QuixBugs.Run_7.commented_mergesort import mergesort
# from QuixBugs.gptTOcode._mergesort import mergesort

testdata = load_json_testcases(mergesort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_mergesort(input_data, expected):
    assert mergesort(*input_data) == expected
