import unittest

from ch04.reverse_iterative import reverse_iterative


class TestReverseIterative(unittest.TestCase):

    def test_empty_sequence(self):
        S = []
        reverse_iterative(S)
        self.assertEqual(S, [])

    def test_single_element_sequence(self):
        S = [5]
        reverse_iterative(S)
        self.assertEqual(S, [5])

    def test_even_elements(self):
        S = [1, 2, 3, 4, 5, 6]
        reverse_iterative(S)
        self.assertEqual(S, [6, 5, 4, 3, 2, 1])

    def test_odd_elements(self):
        S = [2, 7, 1, 8, 3]
        reverse_iterative(S)
        self.assertEqual(S, [3, 8, 1, 7, 2])

    def test_large_input(self):
        S = list(range(1, 10001))
        reverse_iterative(S)
        self.assertEqual(S, list(range(10000, 0, -1)))

