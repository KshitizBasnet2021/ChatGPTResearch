#mutation_5_line_no_9_AOR.py
#
#Yes, there is a bug in the provided code. The return statement at the end of the function should return -1 instead of +1 to indicate that the pattern was not found in the text. Here's the corrected code:
#
def find_brute(T, P):
  n, m = len(T), len(P)
  for i in range(n-m+1):
    k = 0
    while k < m and T[i + k] == P[k]:
      k += 1
    if k == m:
      return i
  return -1
#
#
#