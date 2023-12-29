import unittest

#from ch04.No_Comments.reverse_iterative import reverse_iterative
from Chat_gpt_res_textbook import reverse_iterative

class TestReverseIterativeFunction(unittest.TestCase):

    def test_empty_list(self):
        S = []
        reverse_iterative(S)
        self.assertEqual(S, [])

    def test_single_element(self):
        S = [5]
        reverse_iterative(S)
        self.assertEqual(S, [5])

    def test_even_length_list(self):
        S = [1, 2, 3, 4]
        reverse_iterative(S)
        self.assertEqual(S, [4, 3, 2, 1])

    def test_odd_length_list(self):
        S = [1, 2, 3, 4, 5]
        reverse_iterative(S)
        self.assertEqual(S, [5, 4, 3, 2, 1])

    def test_large_input(self):
        S = list(range(1000))
        reversed_S = list(range(999, -1, -1))
        reverse_iterative(S)
        self.assertEqual(S, reversed_S)

