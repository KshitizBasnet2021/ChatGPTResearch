import unittest

from ch04.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_empty_list(self):
        data = []
        target = 5
        self.assertFalse(binary_search(data, target, 0, len(data) - 1))

    def test_single_element_list_found(self):
        data = [5]
        target = 5
        self.assertTrue(binary_search(data, target, 0, len(data) - 1))

    def test_single_element_list_not_found(self):
        data = [7]
        target = 5
        self.assertFalse(binary_search(data, target, 0, len(data) - 1))

    def test_element_found(self):
        data = [2, 4, 6, 8, 10]
        target = 6
        self.assertTrue(binary_search(data, target, 0, len(data) - 1))

    def test_element_not_found(self):
        data = [2, 4, 6, 8, 10]
        target = 5
        self.assertFalse(binary_search(data, target, 0, len(data) - 1))

    def test_large_input_element_found(self):
        data = list(range(1, 10001, 2))
        target = 7777
        self.assertTrue(binary_search(data, target, 0, len(data) - 1))

    def test_large_input_element_not_found(self):
        data = list(range(2, 10002, 2))
        target = 7777
        self.assertFalse(binary_search(data, target, 0, len(data) - 1))
