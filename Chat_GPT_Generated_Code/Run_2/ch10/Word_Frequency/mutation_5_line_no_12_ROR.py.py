#mutation_5_line_no_12_ROR.py
#
#Yes, there is a bug in the provided code. The bug is in the comparison `if c >= max_count` in the second for loop. The condition should be `if c > max_count` instead, because we want to find the word with the highest frequency, not the word with the highest or equal frequency.
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
#
#