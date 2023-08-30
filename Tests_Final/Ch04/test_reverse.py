import unittest

from ch04.No_Comments.reverse import reverse


class TestReverseFunction(unittest.TestCase):

    def test_empty_list(self):
        S = []
        reverse(S, 0, len(S))
        self.assertEqual(S, [])

    def test_single_element(self):
        S = [5]
        reverse(S, 0, len(S))
        self.assertEqual(S, [5])

    def test_even_length_list(self):
        S = [1, 2, 3, 4]
        reverse(S, 0, len(S))
        self.assertEqual(S, [4, 3, 2, 1])

    def test_odd_length_list(self):
        S = [1, 2, 3, 4, 5]
        reverse(S, 0, len(S))
        self.assertEqual(S, [5, 4, 3, 2, 1])

    def test_large_input(self):
        S = list(range(1000))
        reversed_S = list(range(999, -1, -1))
        reverse(S, 0, len(S))
        self.assertEqual(S, reversed_S)

    def test_partial_reversal(self):
        S = [1, 2, 3, 4, 5]
        reverse(S, 1, 4)
        self.assertEqual(S, [1, 4, 3, 2, 5])

    def test_partial_reversal_single_element(self):
        S = [1, 2, 3, 4, 5]
        reverse(S, 2, 3)
        self.assertEqual(S, [1, 2, 3, 4, 5])

