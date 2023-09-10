#mutation_10_line_no_5_ROR.py
#
#Yes, there is a bug in the provided code. The condition in the while loop is incorrect. It should be `k < m` instead of `k > m`. 
#
#Here's the corrected code:
#
def find_brute(T, P):
  n, m = len(T), len(P)
  for i in range(n-m+1):
    k = 0
    while (k < m and T[i + k] == P[k]):
      k += 1
    if k == m:
      return i
  return -1
#
#
#