#mutation_3_line_no_3_AOR.py
#
#Yes, there is a bug in the provided code. 
#
#The line `A = [0] ** n` is incorrect. It should be `A = [0] * n` to create a list of zeros with length `n`. 
#
#Here is the corrected code:
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