import pytest

# from QuixBugs.Run_6.sieve import sieve
# from QuixBugs.Run_7.commented_sieve import sieve
from load_testdata import load_json_testcases
# from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_sieve import sieve
# from QuixBugs.correct_python_programs.sieve import sieve
#from QuixBugs.gptTOcode._sieve import sieve
from Chat_GPT_Generated_Code.Run_12.sieve import sieve
testdata = load_json_testcases(sieve.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_sieve(input_data, expected):
    assert sieve(*input_data) == expected
