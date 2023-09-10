#mutation_3_line_no_3_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the range of the for loop. The range should be (n - m + 1) instead of (n - m) - 1. 
#
#Here's the corrected code:
#
def find_brute(T, P):
  n, m = len(T), len(P)
  for i in range((n - m) + 1):
    k = 0
    while k < m and T[i + k] == P[k]:
      k += 1
    if k == m:
      return i
  return -1
#
#
#