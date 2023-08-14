import unittest

from ch03.unique import unique1, unique2


# needs to

class TestUnique(unittest.TestCase):

    def test_empty_list(self):
        S = []
        self.assertTrue(unique1(S))
        self.assertTrue(unique2(S))

    def test_single_element_list(self):
        S = [5]
        self.assertTrue(unique1(S))
        self.assertTrue(unique2(S))

    def test_unique_elements(self):
        S = [2, 4, 6, 8, 10]
        self.assertTrue(unique1(S))
        self.assertTrue(unique2(S))

    def test_duplicate_elements(self):
        S = [2, 4, 6, 8, 4]
        self.assertFalse(unique1(S))  # Expecting False since there are duplicates
        self.assertFalse(unique2(S))  # Expecting False since there are duplicates

    def test_mixed_elements(self):
        S = [-3, 2, 1, -5, 4]
        self.assertTrue(unique1(S))
        self.assertTrue(unique2(S))

    def test_large_input(self):
        S = list(range(1, 10001))
        self.assertTrue(unique1(S))
        self.assertTrue(unique2(S))

    def test_large_duplicate_input(self):
        S = [1] * 10000
        self.assertFalse(unique1(S))  # Expecting False since there are duplicates
        self.assertFalse(unique2(S))  # Expecting False since there are duplicates

if __name__ == '__main__':
    unittest.main()
