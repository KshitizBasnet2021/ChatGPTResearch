#mutation_11_line_no_5_ROR.py
#
#Yes, there is a bug in the provided code. The while loop condition should be modified to check if k is less than m instead of less than or equal to m. This is because the index k should only go up to m-1, as the indices of a string start from 0. 
#
#Here is the corrected code:
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