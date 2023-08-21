import unittest

from ch13.Nocomments.find_boyer_moore import find_boyer_moore


class TestBoyerMoore(unittest.TestCase):

    def test_empty_pattern(self):
        self.assertEqual(find_boyer_moore("text", ""), 0)

    def test_exact_match(self):
        self.assertEqual(find_boyer_moore("test", "test"), 0)

    def test_no_match(self):
        self.assertEqual(find_boyer_moore("abcdefg", "xyz"), -1)

    def test_partial_match(self):
        self.assertEqual(find_boyer_moore("abcdefgh", "cde"), 2)

    def test_multiple_matches(self):
        self.assertEqual(find_boyer_moore("ababab", "aba"), 0)
        self.assertEqual(find_boyer_moore("ababab", "bab"), 1)
        self.assertEqual(find_boyer_moore("ababab", "abab"), 0)
        self.assertEqual(find_boyer_moore("ababab", "ab"), 0)

    def test_long_pattern(self):
        self.assertEqual(find_boyer_moore("abcdefg", "defgijkl"), -1)

    def test_long_text(self):
        self.assertEqual(find_boyer_moore("a" * 10000, "a" * 1000), 0)

    def test_case_sensitivity(self):
        self.assertEqual(find_boyer_moore("AbCdEf", "cde"), -1)
        self.assertEqual(find_boyer_moore("AbCdEf", "CdE"), 2)

    def test_unicode_characters(self):
        self.assertEqual(find_boyer_moore("こんにちは", "にち"), 2)

    def test_special_characters(self):
        self.assertEqual(find_boyer_moore("abc$%123#^xyz", "#^x"), 8)

    def test_pattern_longer_than_text(self):
        self.assertEqual(find_boyer_moore("test", "testing"), -1)
