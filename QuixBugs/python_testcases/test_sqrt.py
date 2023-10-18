import pytest

# from QuixBugs.Run_6.sqrt import sqrt
from QuixBugs.Run_7.commented_sqrt import sqrt
from load_testdata import load_json_testcases
# from QuixBugs.correct_python_programs.sqrt import sqrt
#from QuixBugs.gptTOcode._sqrt import sqrt

testdata = load_json_testcases(sqrt.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_sqrt(input_data, expected):
    assert sqrt(*input_data) == pytest.approx(expected, abs=input_data[-1])
