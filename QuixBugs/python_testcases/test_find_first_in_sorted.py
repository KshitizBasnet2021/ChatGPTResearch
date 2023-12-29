import pytest

# from QuixBugs.Run_6.find_first_in_sorted import find_first_in_sorted
# from QuixBugs.Run_7.commented_find_first_in_sorted import find_first_in_sorted

from load_testdata import load_json_testcases
# from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_find_first_in_sorted import find_first_in_sorted
# from QuixBugs.correct_python_programs.find_first_in_sorted import find_first_in_sorted
#from QuixBugs.gptTOcode._find_first_in_sorted import find_first_in_sorted
from Chat_GPT_Generated_Code.Run_12.find_first_in_sorted import find_first_in_sorted
testdata = load_json_testcases(find_first_in_sorted.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_find_first_in_sorted(input_data, expected):
    assert find_first_in_sorted(*input_data) == expected
