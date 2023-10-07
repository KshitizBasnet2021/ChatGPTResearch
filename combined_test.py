
import unittest
#mutation_9_line_no_6_LCR.py
#
#There is a bug in the provided code. The while loop condition should be modified to check if `IlllIIIIIllIlIIIll` is less than `IllllIIlIIIIl` and if the characters at the corresponding positions in the two strings are equal. Additionally, the loop should terminate if `IIlIllIIIIIllIIIl + IlllIIIIIllIlIIIll` exceeds the length of `lIlIlIllIIIIII`. 
#
#Here is the corrected code:
#
def find_brute(lIlIlIllIIIIII, IlIllllIIlIlII):
  IllIIIIlIl, IllllIIlIIIIl = len(lIlIlIllIIIIII), len(IlIllllIIlIlII)                      
  for IIlIllIIIIIllIIIl in range(IllIIIIlIl-IllllIIlIIIIl+1):                     
    IlllIIIIIllIlIIIll = 0                                    
    while (IlllIIIIIllIlIIIll < IllllIIlIIIIl and IIlIllIIIIIllIIIl + IlllIIIIIllIlIIIll < IllIIIIlIl and lIlIlIllIIIIII[IIlIllIIIIIllIIIl + IlllIIIIIllIlIIIll] == IlIllllIIlIlII[IlllIIIIIllIlIIIll]):
      IlllIIIIIllIlIIIll += 1
    if IlllIIIIIllIlIIIll == IllllIIlIIIIl:                               
      return IIlIllIIIIIllIIIl                               
  return -1
#
#
#
import unittest



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
