import unittest

from ch03.prefix_averages import prefix_average1, prefix_average2, prefix_average3


class TestPrefixAverages(unittest.TestCase):

    def test_prefix_average1(self):
        self.assertEqual(prefix_average1([1, 2, 3, 4]), [1.0, 1.5, 2.0, 2.5])
        self.assertEqual(prefix_average1([0, 0, 0, 0]), [0.0, 0.0, 0.0, 0.0])
        self.assertEqual(prefix_average1([5, 5, 5, 5]), [5.0, 5.0, 5.0, 5.0])
        self.assertEqual(prefix_average1([]), [])
        self.assertEqual(prefix_average1([1]), [1.0])
        self.assertEqual(prefix_average1([-1, 1, -1, 1]), [-1.0, 0.0, -0.3333333333333333, 0.0])

    def test_prefix_average2(self):
        self.assertEqual(prefix_average2([1, 2, 3, 4]), [1.0, 1.5, 2.0, 2.5])
        self.assertEqual(prefix_average2([0, 0, 0, 0]), [0.0, 0.0, 0.0, 0.0])
        self.assertEqual(prefix_average2([5, 5, 5, 5]), [5.0, 5.0, 5.0, 5.0])
        self.assertEqual(prefix_average2([]), [])
        self.assertEqual(prefix_average2([1]), [1.0])
        self.assertEqual(prefix_average2([-1, 1, -1, 1]), [-1.0, 0.0, -0.3333333333333333, 0.0])

    def test_prefix_average3(self):
        self.assertEqual(prefix_average3([1, 2, 3, 4]), [1.0, 1.5, 2.0, 2.5])
        self.assertEqual(prefix_average3([0, 0, 0, 0]), [0.0, 0.0, 0.0, 0.0])
        self.assertEqual(prefix_average3([5, 5, 5, 5]), [5.0, 5.0, 5.0, 5.0])
        self.assertEqual(prefix_average3([]), [])
        self.assertEqual(prefix_average3([1]), [1.0])
        self.assertEqual(prefix_average3([-1, 1, -1, 1]), [-1.0, 0.0, -0.3333333333333333, 0.0])

    # Additional Edge Cases
    def test_prefix_average1_edge(self):
        self.assertEqual(prefix_average1([0, 0, 0]), [0.0, 0.0, 0.0])
        self.assertEqual(prefix_average1([-1, 0, 1]), [-1.0, -0.5, 0.0])

    def test_prefix_average2_edge(self):
        self.assertEqual(prefix_average2([0, 0, 0]), [0.0, 0.0, 0.0])
        self.assertEqual(prefix_average2([-1, 0, 1]), [-1.0, -0.5, 0.0])

    def test_prefix_average3_edge(self):
        self.assertEqual(prefix_average3([0, 0, 0]), [0.0, 0.0, 0.0])
        self.assertEqual(prefix_average3([-1, 0, 1]), [-1.0, -0.5, 0.0])

