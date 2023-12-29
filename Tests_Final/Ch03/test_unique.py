import unittest

#from ch03.unique import unique1
from Chat_gpt_res_textbook.unique import unique1

class TestUniqueFunctions(unittest.TestCase):

    def test_empty_list(self):
        S = []
        self.assertTrue(unique1(S))

    def test_single_element(self):
        S = [5]
        self.assertTrue(unique1(S))

    def test_unique_elements(self):
        S = [1, 2, 3, 4, 5]
        self.assertTrue(unique1(S))

    def test_duplicate_elements(self):
        S = [1, 2, 2, 3, 4]
        self.assertFalse(unique1(S))

    def test_mixed_elements(self):
        S = [5, 2, 4, 3, 1]
        self.assertTrue(unique1(S))

    def test_negative_numbers(self):
        S = [-1, -2, -3, -4, -5]
        self.assertTrue(unique1(S))

    def test_mixed_numbers(self):
        S = [1, -2, 3, -4, 5]
        self.assertTrue(unique1(S))

    def test_mixed_duplicates(self):
        S = [1, 2, -3, 2, 1]
        self.assertFalse(unique1(S))

    def test_large_input(self):
        S = list(range(1, 1001))
        self.assertTrue(unique1(S))

    def test_large_duplicate_input(self):
        S = [1] * 1000
        self.assertFalse(unique1(S))

