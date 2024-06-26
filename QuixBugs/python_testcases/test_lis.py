import pytest

# from QuixBugs.Run_6.lis import lis
# from QuixBugs.Run_6.lis import lis
# from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_lis import lis
from Chat_GPT_Generated_Code.Run_12.lis import lis
from load_testdata import load_json_testcases

# from QuixBugs.correct_python_programs.lis import lis
#from QuixBugs.gptTOcode._lis import lis

testdata = load_json_testcases(lis.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_lis(input_data, expected):
    assert lis(*input_data) == expected
