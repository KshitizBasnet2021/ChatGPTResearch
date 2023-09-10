#mutation_8_line_no_19_AOR.py
#
#Yes, there is a bug in the provided code. 
#
#In the else block, when there is a mismatch between T[i] and P[k], the code incorrectly sets k = m + 1 instead of k = m - 1. This will cause the algorithm to skip characters in the pattern P and potentially miss a match.
#
#Here is the corrected code:
#
def find_boyer_moore(T, P):
  n, m = len(T), len(P)
  if m == 0: return 0
  last = {}
  for k in range(m):
    last[ P[k] ] = k
  i = m-1
  k = m-1
  while i < n:
    if T[i] == P[k]:
      if k == 0:
        return i
      else:
        i -= 1
        k -= 1
    else:
      j = last.get(T[i], -1)
      i += m - min(k, j + 1)
      k = m - 1
  return -1
#
#
#