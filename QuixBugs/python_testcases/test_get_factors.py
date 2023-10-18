import pytest

from QuixBugs.Run_6.get_factors import get_factors
# from QuixBugs.Run_7.commented_get_factors import get_factors
from load_testdata import load_json_testcases

# from QuixBugs.correct_python_programs.get_factors import get_factors
#from QuixBugs.gptTOcode._get_factors  import get_factors

testdata = load_json_testcases(get_factors.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_get_factors(input_data, expected):
    assert get_factors(*input_data) == expected
