import unittest

#from ch03.No_Comments.prefix_averages import  prefix_average3
from Chat_gpt_res_textbook.prefix_averages import prefix_average3;

class TestPrefixAverageFunctions(unittest.TestCase):

    def test_empty_list(self):
        S = []
        result3 = prefix_average3(S)
        self.assertEqual(result3, [])

    def test_single_element(self):
        S = [5]
        result3 = prefix_average3(S)
        self.assertEqual(result3, [5.0])

    def test_positive_integers(self):
        S = [1, 2, 3, 4, 5]
        result3 = prefix_average3(S)
        expected = [1.0, 1.5, 2.0, 2.5, 3.0]
        self.assertEqual(result3, expected)

    def test_zeroes(self):
        S = [0, 0, 0, 0, 0]
        result3 = prefix_average3(S)
        expected = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertEqual(result3, expected)


    def test_large_input(self):
        S = list(range(1, 1001))
        result3 = prefix_average3(S)
        expected = [float(sum(S[0:i+1])) / (i+1) for i in range(1000)]
        self.assertEqual(result3, expected)

