import pytest


from load_testdata import load_json_testcases
# from QuixBugs.Run_6.gcd import gcd
# from QuixBugs.Run_7.commented_gcd import gcd
# from QuixBugs.correct_python_programs.gcd import gcd
# from QuixBugs.gptTOcode._gcd import gcd
from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code.gcd import gcd
testdata = load_json_testcases(gcd.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_gcd(input_data, expected):
    assert gcd(*input_data) == expected
