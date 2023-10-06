import pytest
from load_testdata import load_json_testcases

from QuixBugs.correct_python_programs.subsequences import subsequences
#from QuixBugs.gptTOcode._subsequences import subsequences

testdata = load_json_testcases(subsequences.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_subsequences(input_data, expected):
    assert subsequences(*input_data) == expected
