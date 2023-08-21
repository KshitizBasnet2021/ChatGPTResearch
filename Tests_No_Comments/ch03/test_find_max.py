import unittest

from ch03.No_Comments.find_max import find_max


class TestFindMaxFunction(unittest.TestCase):

    def test_single_element(self):
        data = [5]
        result = find_max(data)
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        data = [1, 3, 2, 5, 4]
        result = find_max(data)
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        data = [-1, -3, -2, -5, -4]
        result = find_max(data)
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        data = [-1, 3, -2, 5, -4]
        result = find_max(data)
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        data = [5, 5, 5, 5, 5]
        result = find_max(data)
        self.assertEqual(result, 5)

    def test_large_input(self):
        data = list(range(1000))
        result = find_max(data)
        self.assertEqual(result, 999)

    def test_empty_strings(self):
        data = ['']
        result = find_max(data)
        self.assertEqual(result, '')

    def test_strings(self):
        data = ['apple', 'banana', 'grape', 'cherry']
        result = find_max(data)
        self.assertEqual(result, 'grape')