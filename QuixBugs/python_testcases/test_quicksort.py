import pytest

from QuixBugs.Run_6.quicksort import quicksort
from load_testdata import load_json_testcases

# from QuixBugs.correct_python_programs.quicksort import quicksort
#from QuixBugs.gptTOcode._quicksort import quicksort

testdata = load_json_testcases(quicksort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_quicksort(input_data, expected):
    assert quicksort(*input_data) == expected
