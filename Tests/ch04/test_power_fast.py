import unittest

from ch04.power_fast import power


class TestPowerFunction(unittest.TestCase):

    def test_power_zero_exponent(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(-2, 0), 1)

    def test_power_positive_exponent(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(3, 4), 81)
        self.assertEqual(power(-2, 4), 16)


    def test_power_large_exponent(self):
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(power(10, 5), 100000)

    def test_power_base_zero(self):
        self.assertEqual(power(0, 5), 0)
        self.assertEqual(power(0, 0), 1)