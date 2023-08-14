import unittest

from ch04.power_fast import power


class TestPower(unittest.TestCase):

    def test_power_of_zero(self):
        x = 5
        n = 0
        self.assertEqual(power(x, n), 1)

    def test_power_of_one(self):
        x = 10
        n = 1
        self.assertEqual(power(x, n), 10)

    def test_positive_power(self):
        x = 2
        n = 5
        self.assertEqual(power(x, n), 32)

    def test_negative_power(self):
        x = 3
        n = -3
        self.assertEqual(power(x, n), 1 / 27)

    def test_large_positive_power(self):
        x = 2
        n = 10
        self.assertEqual(power(x, n), 1024)

    def test_large_negative_power(self):
        x = 4
        n = -5
        self.assertEqual(power(x, n), 1 / 1024)

    def test_large_odd_power(self):
        x = 3
        n = 7
        self.assertEqual(power(x, n), 2187)

if __name__ == '__main__':
    unittest.main()
