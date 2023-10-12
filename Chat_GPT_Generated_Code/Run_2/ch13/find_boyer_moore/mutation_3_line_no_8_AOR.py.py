#mutation_3_line_no_8_AOR.py
#
#Yes, there are a few bugs in the provided code. Here are the fixes:
#
#1. In the line `i = m-1`, it should be `i = m - 1` (with a space before the minus sign).
#
#2. In the line `i = m + 1`, it should be `i = m - 1` (to initialize `i` correctly).
#
#3. Inside the while loop, the line `i -= 1` should be moved outside the if-else condition, so that it is always executed.
#
#4. The line `i += m - min(k, j + 1)` should be changed to `i += max(1, k - j)` to correctly calculate the jump distance.
#
#Here's the corrected code:
#
def find_boyer_moore(T, P):
  n, m = len(T), len(P)
  if m == 0: return 0
  last = {}
  for k in range(m):
    last[P[k]] = k
  i = m - 1
  while i < n:
    k = m - 1
    while k >= 0 and T[i] == P[k]:
      i -= 1
      k -= 1
    if k == -1:
      return i + 1
    j = last.get(T[i], -1)
    i += max(1, k - j)
  return -1
#
#
#