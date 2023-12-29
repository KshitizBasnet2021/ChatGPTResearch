import pytest

# from QuixBugs.Run_6.kth import kth
# from QuixBugs.Run_7.commented_kth import kth
from load_testdata import load_json_testcases
# from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_kth import kth
from Chat_GPT_Generated_Code.Run_12.kth import kth
# from QuixBugs.correct_python_programs.kth import kth
#from QuixBugs.gptTOcode._kth import kth

testdata = load_json_testcases(kth.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kth(input_data, expected):
    assert kth(*input_data) == expected
