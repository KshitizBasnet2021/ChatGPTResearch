#mutation_6_line_no_6_ASR.py
#
#Yes, there is a bug in the provided code. In the while loop, the variable `k` should be incremented instead of decremented. 
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