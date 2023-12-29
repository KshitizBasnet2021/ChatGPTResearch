import pytest

# from QuixBugs.Run_6.next_permutation import next_permutation
# from QuixBugs.Run_6.next_permutation import next_permutation
from load_testdata import load_json_testcases
# from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_next_permutation import next_permutation
from Chat_GPT_Generated_Code.Run_12.next_permutation import next_permutation
# from QuixBugs.correct_python_programs.next_permutation import next_permutation
#from QuixBugs.gptTOcode._next_permutation import next_permutation

testdata = load_json_testcases(next_permutation.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_next_permutation(input_data, expected):
    assert next_permutation(*input_data) == expected
