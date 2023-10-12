#mutation_1_line_no_3_AOR.py
#
#Yes, there is a bug in the provided code. 
#
#The bug is in the line `A = [0] / n`. It seems like the intention was to create a list of size `n` with all elements initialized to 0. However, the division operator `/` is used instead of the multiplication operator `*`. 
#
#To fix this bug, we need to change the line to `A = [0] * n`. This will create a list of size `n` with all elements initialized to 0. 
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