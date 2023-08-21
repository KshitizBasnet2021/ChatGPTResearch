import unittest

from ch12.No_Comments.merge_array import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        S = []
        merge_sort(S)
        self.assertEqual(S, [])

    def test_single_element(self):
        S = [1]
        merge_sort(S)
        self.assertEqual(S, [1])

    def test_sorted_list(self):
        S = [1, 2, 3, 4, 5]
        merge_sort(S)
        self.assertEqual(S, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        S = [5, 4, 3, 2, 1]
        merge_sort(S)
        self.assertEqual(S, [1, 2, 3, 4, 5])

    def test_mixed_list(self):
        S = [3, 1, 4, 5, 2]
        merge_sort(S)
        self.assertEqual(S, [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        S = [2, 4, 1, 3, 2]
        merge_sort(S)
        self.assertEqual(S, [1, 2, 2, 3, 4])

    def test_large_list(self):
        S = list(range(10000, 0, -1))
        merge_sort(S)
        self.assertEqual(S, list(range(1, 10001)))

