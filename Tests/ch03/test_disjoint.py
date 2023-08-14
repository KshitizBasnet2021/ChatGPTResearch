import unittest

from ch03.disjoint import disjoint1, disjoint2


class TestDisjoint(unittest.TestCase):

    def test_disjoint1_no_common(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        self.assertTrue(disjoint1(A, B, C))

    def test_disjoint1_common(self):
        A = [1, 2, 3]
        B = [4, 3, 6]
        C = [3, 8, 9]
        self.assertFalse(disjoint1(A, B, C))

    def test_disjoint1_empty_lists(self):
        A = []
        B = []
        C = []
        self.assertTrue(disjoint1(A, B, C))

    def test_disjoint2_no_common(self):
        A = [1, 2, 3]
        B = [4, 5, 6]
        C = [7, 8, 9]
        self.assertTrue(disjoint2(A, B, C))

    def test_disjoint2_common(self):
        A = [1, 2, 3]
        B = [4, 3, 6]
        C = [3, 8, 9]
        self.assertFalse(disjoint2(A, B, C))

    def test_disjoint2_empty_lists(self):
        A = []
        B = []
        C = []
        self.assertTrue(disjoint2(A, B, C))


