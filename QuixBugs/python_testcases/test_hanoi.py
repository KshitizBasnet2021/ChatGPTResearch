import pytest

# from QuixBugs.Run_6.hanoi import hanoi
# from QuixBugs.Run_7.commented_hanoi import hanoi
from load_testdata import load_json_testcases
# from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_hanoi import hanoi
# from QuixBugs.correct_python_programs.hanoi import hanoi
#from QuixBugs.gptTOcode._hanoi import hanoi
from Chat_GPT_Generated_Code.Run_12.hanoi import hanoi
testdata = load_json_testcases(hanoi.__name__)
testdata = [[inp, [tuple(x) for x in out]] for inp, out in testdata]


@pytest.mark.parametrize("input_data,expected", testdata)
def test_hanoi(input_data, expected):
    assert hanoi(*input_data) == expected
