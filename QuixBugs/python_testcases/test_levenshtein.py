import pytest
from load_testdata import load_json_testcases

from QuixBugs.correct_python_programs.levenshtein import levenshtein
#from QuixBugs.gptTOcode._levenshtein import levenshtein

testdata = load_json_testcases(levenshtein.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_levenshtein(input_data, expected):
    if input_data == [
        "amanaplanacanalpanama",
        "docnoteidissentafastneverpreventsafatnessidietoncod",
    ]:
        pytest.skip("Takes too long to pass!")

    assert levenshtein(*input_data) == expected