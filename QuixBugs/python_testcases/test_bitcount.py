import pytest


from load_testdata import load_json_testcases

# from QuixBugs.python_programs.bitcount import bitcount
# from QuixBugs.correct_python_programs.bitcount import bitcount
# from QuixBugs.gptTOcode._bitcount import bitcount
from QuixBugs.Run_6.bitcount import bitcount


testdata = load_json_testcases(bitcount.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_bitcount(input_data, expected):
    assert bitcount(*input_data) == expected
