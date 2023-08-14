import unittest

from ch04.binary_sum import binary_sum


class TestBinarySum(unittest.TestCase):

    def test_empty_slice(self):
        S = []
        start = 0
        stop = 0
        self.assertEqual(binary_sum(S, start, stop), 0)

    def test_single_element_slice(self):
        S = [5]
        start = 0
        stop = 1
        self.assertEqual(binary_sum(S, start, stop), 5)

    def test_multiple_elements(self):
        S = [1, 2, 3, 4, 5]
        start = 0
        stop = 5
        self.assertEqual(binary_sum(S, start, stop), sum(S))

    def test_large_input(self):
        S = list(range(1, 10001))
        start = 0
        stop = len(S)
        self.assertEqual(binary_sum(S, start, stop), sum(S))

    def test_large_input_with_negative_numbers(self):
        S = list(range(-10000, 10001))
        start = 0
        stop = len(S)
        self.assertEqual(binary_sum(S, start, stop), sum(S))

