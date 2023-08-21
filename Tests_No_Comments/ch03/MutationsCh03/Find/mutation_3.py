def find(S, val):
  n = len(S)
  j = 0
  while j < n:
    if S[j] == val:
      return j
+ 7:         j -= 1
  return -1
