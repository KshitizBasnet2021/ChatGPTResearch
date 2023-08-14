import unittest

from ch03.find import find


class TestFind(unittest.TestCase):

    def test_empty_list(self):
        S = []
        val = 5
        self.assertEqual(find(S, val), -1)

    def test_element_present(self):
        S = [1, 2, 3, 4, 5]
        val = 3
        self.assertEqual(find(S, val), 2)

    def test_element_not_present(self):
        S = [1, 2, 3, 4, 5]
        val = 6
        self.assertEqual(find(S, val), -1)

    def test_duplicate_elements(self):
        S = [1, 2, 3, 2, 4]
        val = 2
        self.assertEqual(find(S, val), 1)

    def test_element_present_at_last_index(self):
        S = [1, 2, 3, 4, 5]
        val = 5
        self.assertEqual(find(S, val), 4)

    def test_element_present_at_first_index(self):
        S = [1, 2, 3, 4, 5]
        val = 1
        self.assertEqual(find(S, val), 0)

    def test_element_present_in_single_element_list(self):
        S = [8]
        val = 8
        self.assertEqual(find(S, val), 0)

    def test_element_not_present_in_single_element_list(self):
        S = [8]
        val = 5
        self.assertEqual(find(S, val), -1)

    def test_large_input(self):
        S = list(range(10000, 0, -1))
        val = 5000
        self.assertEqual(find(S, val), 5000)

