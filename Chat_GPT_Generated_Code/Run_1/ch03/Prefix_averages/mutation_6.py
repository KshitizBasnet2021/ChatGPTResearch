#mutation_6_line_no_8_AOR.py
#
#Yes, there is a bug in the provided code. 
#
#In the line `A[j] = total / (j - 1)`, the denominator should be `j + 1` instead of `j - 1`. This is because we want to calculate the average of `S[0]` to `S[j]`, which includes `j + 1` elements.
#
#Here is the corrected code:
#
def prefix_average3(S):
  """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
  n = len(S)
  A = [0] * n                   # create new list of n zeros
  total = 0                     # compute prefix sum as S[0] + S[1] + ...
  for j in range(n):
    total += S[j]               # update prefix sum to include S[j]
    A[j] = total / (j + 1)      # calculate average of S[0] to S[j]
  return A
#
#
#