#mutation_1_line_no_3_AOR.py
#
#There is a bug in the provided code. The condition in the while loop of the merge function should be "i < len(S1) and j < len(S2)" instead of "i - j < len(S)". 
#
#Here is the corrected code:
#
def merge(S1, S2, S):
  i = j = 0
  while i < len(S1) and j < len(S2):
    if S1[i] < S2[j]:
      S[i+j] = S1[i]
      i += 1
    else:
      S[i+j] = S2[j]
      j += 1
  while i < len(S1):
    S[i+j] = S1[i]
    i += 1
  while j < len(S2):
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