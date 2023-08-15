import unittest

from ch13.find_brute import find_brute


class TestFindBrute(unittest.TestCase):

    def test_find_brute_basic(self):
        self.assertEqual(find_brute('hello', 'lo'), 3)
        self.assertEqual(find_brute('abcdef', 'cd'), 2)
        self.assertEqual(find_brute('abcdabcd', 'ab'), 0)
        self.assertEqual(find_brute('abcdef', 'gh'), -1)
        self.assertEqual(find_brute('', ''), 0)

    def test_find_brute_longer_pattern(self):
        self.assertEqual(find_brute('abcde', 'abcdeabcde'), -1)
        self.assertEqual(find_brute('abcdef', 'abcdefabcdef'), -1)

    def test_find_brute_empty_string(self):
        self.assertEqual(find_brute('', 'abc'), -1)
        self.assertEqual(find_brute('abc', ''), 0)

    def test_find_brute_equal_strings(self):
        self.assertEqual(find_brute('abc', 'abc'), 0)
        self.assertEqual(find_brute('abcabc', 'abcabc'), 0)

    def test_find_brute_single_char(self):
        self.assertEqual(find_brute('a', 'a'), 0)
        self.assertEqual(find_brute('a', 'b'), -1)
        self.assertEqual(find_brute('abc', 'b'), 1)

    def test_find_brute_repeated_chars(self):
        self.assertEqual(find_brute('aaaa', 'a'), 0)
        self.assertEqual(find_brute('ababab', 'ab'), 0)
        self.assertEqual(find_brute('ababab', 'ba'), 1)

    def test_find_brute_large_text(self):
        T = 'a' * 1000000 + 'b' * 1000000
        P = 'b' * 1000000
        self.assertEqual(find_brute(T, P), 1000000)
