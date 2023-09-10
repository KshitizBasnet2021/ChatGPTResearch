#mutation_10_line_no_13_COI.py
#
#Yes, there is a bug in the provided code. In the merge_sort function, the condition for the base case is incorrect. Instead of checking if n < 2, it should check if n > 1. 
#
#Here's the corrected code:
#
def merge(S1, S2, S):
  i = j = 0
  while i + j < len(S):
    if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
      S[i+j] = S1[i]
      i += 1
    else:
      S[i+j] = S2[j]
      j += 1
#
def merge_sort(S):
  n = len(S)
  if n > 1:
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)
#
#
#