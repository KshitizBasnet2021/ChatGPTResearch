import unittest

from ch03.disjoint import disjoint1


class TestDisjoint(unittest.TestCase):

    def test_empty_lists(self):
        A = []
        B = []
        C = []
        self.assertTrue(disjoint1(A, B, C))

    def test_disjoint_lists(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        self.assertTrue(disjoint1(A, B, C))

    def test_common_element_disjoint_lists(self):
        A = [1, 2, 3]
        B = [3, 4, 5]
        C = [5, 6, 7]
        self.assertTrue(disjoint1(A, B, C))

    def test_common_element_non_disjoint_lists(self):
        A = [1, 2, 3]
        B = [3, 4, 5]
        C = [5, 6, 3]
        self.assertFalse(disjoint1(A, B, C))

    def test_single_element_lists(self):
        A = [1]
        B = [1]
        C = [1]
        self.assertFalse(disjoint1(A, B, C))