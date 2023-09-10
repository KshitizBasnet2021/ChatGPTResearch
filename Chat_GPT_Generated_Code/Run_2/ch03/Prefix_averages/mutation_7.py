#mutation_7_line_no_6_ASR.py
#
#Yes, there is a bug in the provided code. The bug is in the line `total -= S[j]`. It should be `total += S[j]` instead. 
#
#Here's the corrected code:
#
def prefix_average3(S):
  n = len(S)
  A = [0] * n
  total = 0
  for j in range(n):
    total += S[j]
    A[j] = total / (j+1)
  return A
#
#
#