#mutation_15_line_no_4_ROR.py
#
#The provided code is missing a base case for the merge_sort function. When the length of the input list S is less than 2, the function should return without performing any further operations.
#
#Here is the corrected code:
#
def merge(S1, S2, S):
  i = j = 0
  while i + j < len(S):
    if (j != len(S2) or (i < len(S1) and S1[i] < S2[j])):
      S[i+j] = S1[i]
      i += 1
    else:
      S[i+j] = S2[j]
      j += 1
#
def merge_sort(S):
  n = len(S)
  if n < 2:
    return
  mid = n // 2
  S1 = S[0:mid]
  S2 = S[mid:n]
  merge_sort(S1)
  merge_sort(S2)
  merge(S1, S2, S)
#
#
#