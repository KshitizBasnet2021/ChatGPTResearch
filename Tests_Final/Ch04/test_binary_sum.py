import unittest

#from ch04.No_Comments.binary_sum import binary_sum
from Chat_gpt_res_textbook.binary_sum import binary_sum

class TestBinarySum(unittest.TestCase):

    def test_empty_list(self):
        S = []
        result = binary_sum(S, 0, len(S))
        self.assertEqual(result, 0)

    def test_single_element(self):
        S = [5]
        result = binary_sum(S, 0, len(S))
        self.assertEqual(result, 5)

    def test_positive_integers(self):
        S = [1, 2, 3, 4, 5]
        result = binary_sum(S, 0, len(S))
        self.assertEqual(result, sum(S))

    def test_negative_integers(self):
        S = [-1, -2, -3, -4, -5]
        result = binary_sum(S, 0, len(S))
        self.assertEqual(result, sum(S))

    def test_mixed_integers(self):
        S = [-1, 2, -3, 4, -5]
        result = binary_sum(S, 0, len(S))
        self.assertEqual(result, sum(S))

    def test_large_input(self):
        S = list(range(1000))
        result = binary_sum(S, 0, len(S))
        self.assertEqual(result, sum(S))
