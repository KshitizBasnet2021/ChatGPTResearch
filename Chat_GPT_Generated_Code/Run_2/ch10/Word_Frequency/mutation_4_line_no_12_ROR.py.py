#mutation_4_line_no_12_ROR.py
#
#Yes, there is a bug in the provided code. The bug is in the second for loop where it checks if the count of a word is less than the current maximum count. It should be checking if the count is greater than the current maximum count instead.
#
#Here's the fixed code:
#
def find_most_frequent_word(filename):
  freq = {}
  with open(filename) as file:
    for piece in file.read().lower().split():
      word = ''.join(c for c in piece if c.isalpha())
      if word:
        freq[word] = 1 + freq.get(word, 0)
#
  max_word = ''
  max_count = 0
  for (w, c) in freq.items():
    if c > max_count:
      max_word = w
      max_count = c
#
  return max_word, max_count
#
#Now the code should correctly find the most frequent word in the given file.
#
#
#