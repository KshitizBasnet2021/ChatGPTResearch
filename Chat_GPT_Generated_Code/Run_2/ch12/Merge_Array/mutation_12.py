#mutation_12_line_no_4_LCR.py
#
#There is a bug in the provided code. In the if condition inside the while loop of the merge function, the comparison operator should be <= instead of < for checking if i is less than len(S1). 
#
#Here is the corrected code:
#
def merge(S1, S2, S):
  i = j = 0
  while i + j < len(S):
    if (j == len(S2) or (i < len(S1) and S1[i] <= S2[j])):
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