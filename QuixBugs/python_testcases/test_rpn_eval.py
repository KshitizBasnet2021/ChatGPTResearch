import pytest

# from QuixBugs.Run_6.rpn_eval import rpn_eval
# from QuixBugs.Run_7.commented_rpn_eval import rpn_eval
from load_testdata import load_json_testcases
# from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_rpn_eval import rpn_eval
# from QuixBugs.correct_python_programs.rpn_eval import rpn_eval
#from QuixBugs.gptTOcode._rpn_eval import rpn_eval
from Chat_GPT_Generated_Code.Run_12.rpn_eval import rpn_
testdata = load_json_testcases(rpn_eval.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_rpn_eval(input_data, expected):
    assert rpn_eval(*input_data) == expected
