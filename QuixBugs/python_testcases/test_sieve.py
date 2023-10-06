import pytest
from load_testdata import load_json_testcases

from QuixBugs.correct_python_programs.sieve import sieve
#from QuixBugs.gptTOcode._sieve import sieve

testdata = load_json_testcases(sieve.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_sieve(input_data, expected):
    assert sieve(*input_data) == expected
