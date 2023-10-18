import pytest

# from QuixBugs.Run_6.bucketsort import bucketsort
from QuixBugs.Run_7.commented_bucketsort import bucketsort
from load_testdata import load_json_testcases

# from QuixBugs.python_programs.bucketsort import bucketsort
# from QuixBugs.gptTOcode._bucketsort import bucketsort
# from QuixBugs.correct_python_programs.bucketsort import bucketsort

testdata = load_json_testcases(bucketsort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_bucketsort(input_data, expected):
    assert bucketsort(*input_data) == expected
