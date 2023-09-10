#mutation_15_line_no_12_COI.py
#
#There is a bug in the provided code. The bug occurs when the character at index i in the text T does not match the character at index k in the pattern P, and k is not equal to 0. In this case, the code incorrectly decrements both i and k by 1. 
#
#To fix this bug, we need to update the code to correctly handle this case. Instead of decrementing both i and k by 1, we should update i to the next index where the character at T[i] is equal to the last occurrence of P[k] in the pattern. This can be done by using the last dictionary to get the last occurrence of T[i] and updating i accordingly. 
#
#Here is the corrected code:
#
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
    if not (T[i] == P[k]):
      j = last.get(T[i], -1)              # last(T[i]) is -1 if not found
      i += m - min(k, j + 1)              # update i based on last occurrence
      k = m - 1                           # restart at end of pattern
    else:
      if k == 0:
        return i                          # pattern begins at index i of text
      else:
        i -= 1                            # examine previous character
        k -= 1                            # of both T and P
  return -1
#
#
#