import pytest

# from QuixBugs.Run_6.lcs_length import lcs_length
# from QuixBugs.Run_7.commented_lcs_length import lcs_length
from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_lcs_length import lcs_length
from load_testdata import load_json_testcases

# from QuixBugs.correct_python_programs.lcs_length import lcs_length
#from QuixBugs.gptTOcode._lcs_length import lcs_length

testdata = load_json_testcases(lcs_length.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_lcs_length(input_data, expected):
    assert lcs_length(*input_data) == expected
