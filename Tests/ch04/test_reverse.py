import unittest

from ch04.reverse import reverse


class TestReverse(unittest.TestCase):

    def test_empty_slice(self):
        S = []
        start = 0
        stop = 0
        reverse(S, start, stop)
        self.assertEqual(S, [])

    def test_single_element_slice(self):
        S = [5]
        start = 0
        stop = 1
        reverse(S, start, stop)
        self.assertEqual(S, [5])

    def test_even_elements(self):
        S = [1, 2, 3, 4, 5, 6]
        start = 0
        stop = 6
        reverse(S, start, stop)
        self.assertEqual(S, [6, 5, 4, 3, 2, 1])

    def test_odd_elements(self):
        S = [2, 7, 1, 8, 3]
        start = 0
        stop = 5
        reverse(S, start, stop)
        self.assertEqual(S, [3, 8, 1, 7, 2])

    def test_large_input(self):
        S = list(range(1, 10001))
        start = 0
        stop = len(S)
        reverse(S, start, stop)
        self.assertEqual(S, list(range(10000, 0, -1)))

if __name__ == '__main__':
    unittest.main()
