import unittest

from ch13.Nocomments.find_brute import find_brute


class TestBruteForce(unittest.TestCase):

    def test_empty_pattern(self):
        self.assertEqual(find_brute("text", ""), 0)

    def test_exact_match(self):
        self.assertEqual(find_brute("test", "test"), 0)

    def test_no_match(self):
        self.assertEqual(find_brute("abcdefg", "xyz"), -1)

    def test_partial_match(self):
        self.assertEqual(find_brute("abcdefgh", "cde"), 2)

    def test_multiple_matches(self):
        self.assertEqual(find_brute("ababab", "aba"), 0)
        self.assertEqual(find_brute("ababab", "bab"), 1)
        self.assertEqual(find_brute("ababab", "abab"), 0)
        self.assertEqual(find_brute("ababab", "ab"), 0)

    def test_long_pattern(self):
        self.assertEqual(find_brute("abcdefg", "defgijkl"), -1)

    def test_long_text(self):
        self.assertEqual(find_brute("a" * 10000, "a" * 1000), 0)

    def test_case_sensitivity(self):
        self.assertEqual(find_brute("AbCdEf", "cde"), -1)
        self.assertEqual(find_brute("AbCdEf", "CdE"), 2)

    def test_unicode_characters(self):
        self.assertEqual(find_brute("こんにちは", "にち"), 2)

    def test_special_characters(self):
        self.assertEqual(find_brute("abc$%123#^xyz", "#^x"), 8)

    def test_pattern_longer_than_text(self):
        self.assertEqual(find_brute("test", "testing"), -1)
