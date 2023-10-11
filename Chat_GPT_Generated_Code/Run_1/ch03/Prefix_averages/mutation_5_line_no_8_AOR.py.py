#mutation_5_line_no_8_AOR.py
#
#Yes, there is a bug in the provided code. The calculation of the prefix average is incorrect. Instead of multiplying the prefix sum by (j + 1), it should be divided by (j + 1) to get the average.
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
    A[j] = total / (j + 1)      # calculate the average and store in A[j]
  return A
#
#
#