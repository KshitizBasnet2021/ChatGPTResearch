#mutation_2_line_no_5_AOR.py
#
#There is a bug in the provided code. In the merge function, when merging the elements from S1 and S2 into S, the indices used to access the elements of S1 and S2 are incorrect. 
#
#To fix this bug, you need to update the indices used to access the elements of S1 and S2 in the merge function. 
#
#Here is the corrected code:
#
def merge(S1, S2, S):
  i = j = 0
  while i + j < len(S):
    if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
      S[i + j] = S1[i]
      i += 1
    else:
      S[i + j] = S2[j]
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