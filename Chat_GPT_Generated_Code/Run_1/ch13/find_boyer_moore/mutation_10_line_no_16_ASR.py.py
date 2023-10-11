#mutation_10_line_no_16_ASR.py
#
#There is a bug in the provided code. The bug is in the line `i += m - min(k, j + 1)`. This line is used to calculate the jump step when a mismatch occurs. However, the calculation is incorrect.
#
#To fix the bug, we need to change the line to `i += max(1, k - j)`. This will ensure that the jump step is at least 1, and it will correctly handle cases where the last occurrence of the mismatched character in the pattern is to the left of the current position in the text.
#
#Here is the corrected code:
#
#```python
def find_boyer_moore(T, P):
  """Return the lowest index of T at which substring P begins (or else -1)."""
  n, m = len(T), len(P)                   # introduce convenient notations
  if m == 0: return 0                     # trivial search for empty string
  last = {}                               # build 'last' dictionary
  for k in range(m):
    last[ P[k] ] = k                      # later occurrence overwrites
  # align end of pattern at index m-1 of text
  i = m-1                                 # an index into T
  k = m-1                                 # an index into P
  while i < n:
    if T[i] == P[k]:                      # a matching character
      if k == 0:
        return i                          # pattern begins at index i of text
      else:
        i += 1
        k -= 1                            # of both T and P
    else:
      j = last.get(T[i], -1)              # last(T[i]) is -1 if not found
      i += max(1, k - j)                  # case analysis for jump step
      k = m - 1                           # restart at end of pattern
  return -1
#```
#
#With this fix, the `find_boyer_moore` function should work correctly.
#
#
#