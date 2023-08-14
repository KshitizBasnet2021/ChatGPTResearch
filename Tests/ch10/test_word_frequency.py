import unittest
from io import StringIO
import sys
from ch10.word_frequency import *

class TestFindMostFrequentWord(unittest.TestCase):

    def test_empty_file(self):
        with open('empty.txt', 'w') as f:
            pass
        filename = 'empty.txt'
        self.assertEqual(find_most_frequent_word(filename), ('', 0))

    def test_single_word(self):
        with open('single_word.txt', 'w') as f:
            f.write("hello")
        filename = 'single_word.txt'
        self.assertEqual(find_most_frequent_word(filename), ('hello', 1))

    def test_multiple_words(self):
        with open('multiple_words.txt', 'w') as f:
            f.write("hello world hello")
        filename = 'multiple_words.txt'
        self.assertEqual(find_most_frequent_word(filename), ('hello', 2))

    def test_words_with_punctuation(self):
        with open('punctuation.txt', 'w') as f:
            f.write("Hello, world! Hello.")
        filename = 'punctuation.txt'
        self.assertEqual(find_most_frequent_word(filename), ('hello', 2))

    def test_case_insensitivity(self):
        with open('case_insensitivity.txt', 'w') as f:
            f.write("Hello hello HELLO")
        filename = 'case_insensitivity.txt'
        self.assertEqual(find_most_frequent_word(filename), ('hello', 3))

if __name__ == '__main__':
    unittest.main()
