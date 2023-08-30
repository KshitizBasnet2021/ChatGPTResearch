import unittest

from ch03.find import find


class TestFindFunction(unittest.TestCase):

    def test_empty_list(self):
        S = []
        val = 5
        result = find(S, val)
        self.assertEqual(result, -1)

    def test_single_element_found(self):
        S = [5]
        val = 5
        result = find(S, val)
        self.assertEqual(result, 0)

    def test_single_element_not_found(self):
        S = [10]
        val = 5
        result = find(S, val)
        self.assertEqual(result, -1)

    def test_element_found_first_position(self):
        S = [1, 2, 3, 4, 5]
        val = 1
        result = find(S, val)
        self.assertEqual(result, 0)

    def test_element_found_last_position(self):
        S = [1, 2, 3, 4, 5]
        val = 5
        result = find(S, val)
        self.assertEqual(result, 4)

    def test_element_found_middle_position(self):
        S = [1, 2, 3, 4, 5]
        val = 3
        result = find(S, val)
        self.assertEqual(result, 2)

    def test_element_not_found(self):
        S = [1, 2, 3, 4, 5]
        val = 10
        result = find(S, val)
        self.assertEqual(result, -1)

    def test_large_input(self):
        S = list(range(1000))
        val = 500
        result = find(S, val)
        self.assertEqual(result, 500)