import unittest

from ch03.find_max import find_max


class TestFindMax(unittest.TestCase):

    def test_positive_numbers(self):
        data = [1, 5, 3, 9, 2]
        self.assertEqual(find_max(data), 9)

    def test_negative_numbers(self):
        data = [-4, -1, -10, -5]
        self.assertEqual(find_max(data), -1)

    def test_mixed_positive_negative_numbers(self):
        data = [-2, 0, 3, -1, 5]
        self.assertEqual(find_max(data), 5)

    def test_duplicates(self):
        data = [8, 8, 8, 8, 8]
        self.assertEqual(find_max(data), 8)

    def test_single_element_list(self):
        data = [3]
        self.assertEqual(find_max(data), 3)

    def test_large_input(self):
        data = list(range(1, 10001))
        self.assertEqual(find_max(data), 10000)