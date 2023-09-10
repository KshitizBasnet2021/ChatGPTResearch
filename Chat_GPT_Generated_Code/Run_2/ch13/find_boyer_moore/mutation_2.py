#mutation_2_line_no_20_AOD.py
#
#There is a bug in the provided code. The bug is in the line `i += m - min(k, j + 1)`. This line should be `i += max(1, k - j)`. 
#
#Here is the corrected code:
#
#```python
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
      i += max(1, k - j)
      k = m - 1
  return -1
#```
#
#This fix ensures that the algorithm moves the pattern P as far as possible to the right in the text T when a mismatch occurs.
#
#
#