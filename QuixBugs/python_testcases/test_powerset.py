import pytest

# from QuixBugs.Run_6.powerset import powerset
# from QuixBugs.Run_7.commented_powerset import powerset
from load_testdata import load_json_testcases
from QuixBugs.gptTOcodeNonCommented.QuixBugs_Non_commented_py_code_powerset import powerset
# from QuixBugs.correct_python_programs.powerset import powerset
# from QuixBugs.gptTOcode._powerset import powerset

testdata = load_json_testcases(powerset.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_powerset(input_data, expected):
    assert powerset(*input_data) == expected
