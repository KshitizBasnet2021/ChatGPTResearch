import pytest

# from QuixBugs.Run_6.quicksort import quicksort
# from QuixBugs.Run_7.commented_quicksort import quicksort
from load_testdata import load_json_testcases
# from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_quicksort import quicksort
# from QuixBugs.correct_python_programs.quicksort import quicksort
#from QuixBugs.gptTOcode._quicksort import quicksort
from Chat_GPT_Generated_Code.Run_12.quicksort import quicksort
testdata = load_json_testcases(quicksort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_quicksort(input_data, expected):
    assert quicksort(*input_data) == expected
