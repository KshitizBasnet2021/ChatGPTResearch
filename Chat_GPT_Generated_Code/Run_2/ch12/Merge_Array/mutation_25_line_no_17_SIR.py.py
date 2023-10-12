#mutation_25_line_no_17_SIR.py
#
#The provided code is missing the base case for the merge_sort function. It should return when the length of the list is less than or equal to 1. Additionally, the merge function is missing a condition for when the elements in S1 and S2 are equal. Here's the corrected code:
#
def merge(S1, S2, S):
  i = j = 0
  while i + j < len(S):
    if j == len(S2) or (i < len(S1) and S1[i] <= S2[j]):
      S[i+j] = S1[i]
      i += 1
    else:
      S[i+j] = S2[j]
      j += 1
#
def merge_sort(S):
  n = len(S)
  if n <= 1:
    return
  mid = n // 2
  S1 = S[0:mid]
  S2 = S[mid:]
  merge_sort(S1)
  merge_sort(S2)
  merge(S1, S2, S)
#
#
#