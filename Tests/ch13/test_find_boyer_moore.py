import unittest

from ch13.find_boyer_moore import find_boyer_moore


class TestFindBoyerMoore(unittest.TestCase):

    def test_find_boyer_moore_basic(self):
        self.assertEqual(find_boyer_moore('hello', 'lo'), 3)
        self.assertEqual(find_boyer_moore('abcdef', 'cd'), 2)
        self.assertEqual(find_boyer_moore('abcdabcd', 'ab'), 0)
        self.assertEqual(find_boyer_moore('abcdef', 'gh'), -1)
        self.assertEqual(find_boyer_moore('', ''), 0)

    def test_find_boyer_moore_longer_pattern(self):
        self.assertEqual(find_boyer_moore('abcde', 'abcdeabcde'), -1)
        self.assertEqual(find_boyer_moore('abcdef', 'abcdefabcdef'), -1)

    def test_find_boyer_moore_empty_string(self):
        self.assertEqual(find_boyer_moore('', 'abc'), -1)
        self.assertEqual(find_boyer_moore('abc', ''), 0)

    def test_find_boyer_moore_equal_strings(self):
        self.assertEqual(find_boyer_moore('abc', 'abc'), 0)
        self.assertEqual(find_boyer_moore('abcabc', 'abcabc'), 0)

    def test_find_boyer_moore_single_char(self):
        self.assertEqual(find_boyer_moore('a', 'a'), 0)
        self.assertEqual(find_boyer_moore('a', 'b'), -1)
        self.assertEqual(find_boyer_moore('abc', 'b'), 1)

    def test_find_boyer_moore_repeated_chars(self):
        self.assertEqual(find_boyer_moore('aaaa', 'a'), 0)
        self.assertEqual(find_boyer_moore('ababab', 'ab'), 0)
        self.assertEqual(find_boyer_moore('ababab', 'ba'), 1)
        self.assertEqual(find_boyer_moore('ababab', 'baba'), -1)

    def test_find_boyer_moore_large_text(self):
        T = 'a' * 1000000 + 'b' * 1000000
        P = 'b' * 1000000
        self.assertEqual(find_boyer_moore(T, P), 1000000)


if __name__ == '__main__':
    unittest.main()
