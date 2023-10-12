#mutation_8_line_no_7_COI.py
#
#Yes, there is a bug in the provided code. The condition `if not (k == m)` should be changed to `if k == m` in order to correctly check if the pattern has been found. 
#
#Here's the corrected code:
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