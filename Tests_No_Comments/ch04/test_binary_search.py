import unittest

from ch04.No_Comments.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_empty_list(self):
        data = []
        target = 5
        result = binary_search(data, target, 0, len(data) - 1)
        self.assertFalse(result)

    def test_single_element_found(self):
        data = [5]
        target = 5
        result = binary_search(data, target, 0, len(data) - 1)
        self.assertTrue(result)

    def test_single_element_not_found(self):
        data = [10]
        target = 5
        result = binary_search(data, target, 0, len(data) - 1)
        self.assertFalse(result)

    def test_even_length_list_found(self):
        data = [1, 3, 5, 7]
        target = 5
        result = binary_search(data, target, 0, len(data) - 1)
        self.assertTrue(result)

    def test_even_length_list_not_found(self):
        data = [1, 3, 5, 7]
        target = 4
        result = binary_search(data, target, 0, len(data) - 1)
        self.assertFalse(result)

    def test_odd_length_list_found(self):
        data = [2, 4, 6, 8, 10]
        target = 6
        result = binary_search(data, target, 0, len(data) - 1)
        self.assertTrue(result)

    def test_odd_length_list_not_found(self):
        data = [2, 4, 6, 8, 10]
        target = 5
        result = binary_search(data, target, 0, len(data) - 1)
        self.assertFalse(result)

    def test_large_list_found(self):
        data = list(range(1000))
        target = 500
        result = binary_search(data, target, 0, len(data) - 1)
        self.assertTrue(result)

    def test_large_list_not_found(self):
        data = list(range(1000))
        target = 1001
        result = binary_search(data, target, 0, len(data) - 1)
        self.assertFalse(result)
