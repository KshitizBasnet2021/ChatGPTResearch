def find_most_frequent_word(filename):
  freq = {}
  with open(filename) as file:
    for piece in file.read().lower().split():
      word = ''.join(c for c in piece if c.isalpha())
      if word:
        freq[word] = 1 + freq.get(word, 0)

  max_count = max(freq.values())
  max_words = [word for word, count in freq.items() if count == max_count]

  return max_words, max_count