import pytest
from load_testdata import load_json_testcases

from QuixBugs.python_programs.to_base import to_base
# from QuixBugs.gptTOcode._to_base import to_base no need

testdata = load_json_testcases(to_base.__name__)


@pytest.mark.parametrize("input_data,expected", testdata)
def test_to_base(input_data, expected):
    assert to_base(*input_data) == expected
