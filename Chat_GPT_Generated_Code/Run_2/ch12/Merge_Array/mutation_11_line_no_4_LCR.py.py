#mutation_11_line_no_4_LCR.py
#
#Yes, there is a bug in the provided code. In the first if condition inside the while loop of the merge function, the condition should be `S1[i] <= S2[j]` instead of `S1[i] < S2[j]`. This is because we want to include equal elements from both S1 and S2 in the merged list.
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