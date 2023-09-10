#mutation_1_line_no_17_AOD.py
#
#The code provided is missing a check for the case when the pattern length is greater than the text length. This can lead to an index out of range error. To fix this, we can add a check at the beginning of the function to return -1 if the pattern length is greater than the text length.
#
#Here's the updated code:
#
def find_boyer_moore(T, P):
  n, m = len(T), len(P)
  if m == 0 or m > n: return -1
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
#Now, if the pattern length is greater than the text length, the function will return -1.
#
#
#