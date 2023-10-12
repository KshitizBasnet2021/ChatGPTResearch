#mutation_1_line_no_9_AOD.py
#
#The code provided seems to have a bug in the return statement. 
#
#Currently, the code returns 1 if no match is found. However, it would be more appropriate to return -1 to indicate that no match is found. 
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