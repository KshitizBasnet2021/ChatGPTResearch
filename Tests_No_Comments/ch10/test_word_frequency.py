import unittest

from ch10.No_comments.word_frequency import find_most_frequent_word


class TestFindMostFrequentWord(unittest.TestCase):

    def test_empty_file(self):
        result = find_most_frequent_word('empty.txt')
        self.assertEqual(result, ('', 0))

    def test_single_word(self):
        result = find_most_frequent_word('single_word.txt')
        self.assertEqual(result, ('hello', 1))

    def test_multiple_words(self):
        result = find_most_frequent_word('multiple_words.txt')
        self.assertEqual(result, ('hello', 2))

    def test_case_insensitivity(self):
        result = find_most_frequent_word('case_insensitivity.txt')
        self.assertEqual(result, ('hello', 3))

    def test_punctuation_only(self):
        result = find_most_frequent_word('punctuation.txt')
        self.assertEqual(result, ('hello', 2))
