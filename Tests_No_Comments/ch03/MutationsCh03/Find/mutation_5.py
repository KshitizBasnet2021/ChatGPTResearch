def find(S, val):
  n = len(S)
  j = 0
  while j < n:
+ 5:         if not (S[j] == val):
      return j
    j += 1
  return -1
