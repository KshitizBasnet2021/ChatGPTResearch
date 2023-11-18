import pytest

# from QuixBugs.Run_6.subsequences import subsequences
# from QuixBugs.Run_7.commented_subsequences import subsequences
from load_testdata import load_json_testcases
from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_subsequences import subsequences
# from QuixBugs.correct_python_programs.subsequences import subsequences
#from QuixBugs.gptTOcode._subsequences import subsequences

testdata = load_json_testcases(subsequences.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_subsequences(input_data, expected):
    assert subsequences(*input_data) == expected
