import unittest

from ch06.match_delimiters import is_matched


class TestIsMatched(unittest.TestCase):

    def test_empty_expression(self):
        self.assertTrue(is_matched(""))

    def test_single_opening_delimiter(self):
        self.assertFalse(is_matched("("))

    def test_single_closing_delimiter(self):
        self.assertFalse(is_matched(")"))

    def test_correctly_matched(self):
        self.assertTrue(is_matched("()"))
        self.assertTrue(is_matched("([])"))
        self.assertTrue(is_matched("{[()]}"))

    def test_incorrectly_matched(self):
        self.assertFalse(is_matched("("))
        self.assertFalse(is_matched(")"))
        self.assertFalse(is_matched("([)]"))
        self.assertFalse(is_matched("{[}]"))
        self.assertFalse(is_matched("{{)}"))

    def test_complex_expression(self):
        self.assertTrue(is_matched("((()))"))
        self.assertTrue(is_matched("{[()]}"))
        self.assertFalse(is_matched("((()))]"))
        self.assertFalse(is_matched("{[()]}("))

if __name__ == '__main__':
    unittest.main()
