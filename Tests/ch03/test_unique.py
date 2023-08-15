import unittest

from ch03.unique import unique2, unique1


class TestUniqueFunctions(unittest.TestCase):

    def test_unique1_empty_list(self):
        self.assertTrue(unique1([]))

    def test_unique1_single_element_list(self):
        self.assertTrue(unique1([1]))

    def test_unique1_all_unique_elements(self):
        self.assertTrue(unique1([1, 2, 3, 4]))

    def test_unique1_duplicate_elements(self):
        self.assertFalse(unique1([1, 2, 3, 1]))

    def test_unique1_same_elements(self):
        self.assertFalse(unique1([1, 1, 1, 1]))

    def test_unique2_empty_list(self):
        self.assertTrue(unique2([]))

    def test_unique2_single_element_list(self):
        self.assertTrue(unique2([1]))

    def test_unique2_all_unique_elements(self):
        self.assertTrue(unique2([1, 2, 3, 4]))

    def test_unique2_duplicate_elements(self):
        self.assertTrue(unique2([1, 2, 3, 1]))
        self.assertFalse(unique2([3, 2, 1, 1]))

    def test_unique2_same_elements(self):
        self.assertFalse(unique2([1, 1, 1, 1]))

