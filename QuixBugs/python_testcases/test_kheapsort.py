import pytest

from QuixBugs.Run_6.kheapsort import kheapsort
from load_testdata import load_json_testcases

# from QuixBugs.correct_python_programs.kheapsort import kheapsort
# from QuixBugs.gptTOcode._kheapsort import kheapsort

testdata = load_json_testcases(kheapsort.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_kheapsort(input_data, expected):
    assert list(kheapsort(*input_data)) == expected
