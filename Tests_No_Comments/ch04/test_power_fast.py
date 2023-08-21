import unittest

from ch04.No_Comments.power_fast import power


class TestPowerFunction(unittest.TestCase):

    def test_base_case(self):
        result = power(2, 0)
        self.assertEqual(result, 1)

    def test_positive_exponent(self):
        result = power(2, 3)
        self.assertEqual(result, 8)


    def test_large_exponent(self):
        result = power(2, 10)
        self.assertEqual(result, 1024)

    def test_zero_base(self):
        result = power(0, 5)
        self.assertEqual(result, 0)

    def test_zero_exponent(self):
        result = power(5, 0)
        self.assertEqual(result, 1)

    def test_negative_base(self):
        result = power(-2, 3)
        self.assertEqual(result, -8)

    def test_fractional_base(self):
        result = power(0.5, 2)
        self.assertAlmostEqual(result, 0.25)


    def test_fractional_exponent_negative_base(self):
        result = power(-4, 0.5)
        self.assertRaises(ValueError)
