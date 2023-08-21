import unittest

from ch05.No_Comments.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_empty_list(self):
        A = []
        insertion_sort(A)
        self.assertEqual(A, [])

    def test_sorted_list(self):
        A = [1, 2, 3, 4, 5]
        insertion_sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        A = [5, 4, 3, 2, 1]
        insertion_sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5])

    def test_mixed_list(self):
        A = [3, 1, 4, 2, 5]
        insertion_sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        A = [3, 1, 4, 2, 1]
        insertion_sort(A)
        self.assertEqual(A, [1, 1, 2, 3, 4])

    def test_single_element(self):
        A = [1]
        insertion_sort(A)
        self.assertEqual(A, [1])

    def test_large_input(self):
        A = list(range(1000))
        insertion_sort(A)
        self.assertEqual(A, list(range(1000)))

    def test_negative_numbers(self):
        A = [-3, 1, -4, 2, -5]
        insertion_sort(A)
        self.assertEqual(A, [-5, -4, -3, 1, 2])
