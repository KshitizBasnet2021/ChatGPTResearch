import pytest

# from QuixBugs.Run_6.wrap import wrap
# from QuixBugs.Run_7.commented_wrap import wrap
from load_testdata import load_json_testcases
from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_wrap import wrap
# from QuixBugs.correct_python_programs.wrap import wrap
#from QuixBugs.gptTOcode._wrap import wrap

testdata = load_json_testcases(wrap.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_wrap(input_data, expected):
    assert wrap(*input_data) == expected
