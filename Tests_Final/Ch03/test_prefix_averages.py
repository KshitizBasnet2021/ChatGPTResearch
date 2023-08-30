import unittest

from ch03.prefix_averages import prefix_average2, prefix_average3, prefix_average1


class TestPrefixAverageFunctions(unittest.TestCase):

    def test_empty_list(self):
        S = []
        result1 = prefix_average1(S)
        result2 = prefix_average2(S)
        result3 = prefix_average3(S)
        self.assertEqual(result1, [])
        self.assertEqual(result2, [])
        self.assertEqual(result3, [])

    def test_single_element(self):
        S = [5]
        result1 = prefix_average1(S)
        result2 = prefix_average2(S)
        result3 = prefix_average3(S)
        self.assertEqual(result1, [5.0])
        self.assertEqual(result2, [5.0])
        self.assertEqual(result3, [5.0])

    def test_positive_integers(self):
        S = [1, 2, 3, 4, 5]
        result1 = prefix_average1(S)
        result2 = prefix_average2(S)
        result3 = prefix_average3(S)
        expected = [1.0, 1.5, 2.0, 2.5, 3.0]
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)

    def test_zeroes(self):
        S = [0, 0, 0, 0, 0]
        result1 = prefix_average1(S)
        result2 = prefix_average2(S)
        result3 = prefix_average3(S)
        expected = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)

    def test_mixed_integers(self):
        S = [-1, 2, -3, 4, -5]
        result1 = prefix_average1(S)
        result2 = prefix_average2(S)
        result3 = prefix_average3(S)
        expected = [-1.0, 0.5, -0.6666666666666666, 0.5, -0.6]
        for r1, r2, r3, e in zip(result1, result2, result3, expected):
            self.assertAlmostEqual(r1, e)
            self.assertAlmostEqual(r2, e)
            self.assertAlmostEqual(r3, e)

    def test_large_input(self):
        S = list(range(1, 1001))
        result1 = prefix_average1(S)
        result2 = prefix_average2(S)
        result3 = prefix_average3(S)
        expected = [float(sum(S[0:i+1])) / (i+1) for i in range(1000)]
        self.assertEqual(result1, expected)
        self.assertEqual(result2, expected)
        self.assertEqual(result3, expected)

