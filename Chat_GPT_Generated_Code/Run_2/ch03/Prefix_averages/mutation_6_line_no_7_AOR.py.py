#mutation_6_line_no_7_AOR.py
#
#Yes, there is a bug in the provided code. 
#
#The bug is in the line `A[j] = total / (j - 1)`. The denominator should be `j + 1` instead of `j - 1`. 
#
#Here is the corrected code:
#
def prefix_average3(S):
  n = len(S)
  A = [0] * n
  total = 0
  for j in range(n):
    total += S[j]
    A[j] = total / (j + 1)
  return A
#
#
#