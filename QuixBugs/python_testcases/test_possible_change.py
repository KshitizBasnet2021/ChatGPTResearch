import pytest

# from QuixBugs.Run_6.possible_change import possible_change
# from QuixBugs.Run_7.commented_possible_change import possible_change
from load_testdata import load_json_testcases
# from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_possible_change import possible_change
# from QuixBugs.correct_python_programs.possible_change import possible_change
#from QuixBugs.gptTOcode._possible_change import possible_change
from Chat_GPT_Generated_Code.Run_12.possible_change import possible_change
testdata = load_json_testcases(possible_change.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_possible_change(input_data, expected):
    assert possible_change(*input_data) == expected
