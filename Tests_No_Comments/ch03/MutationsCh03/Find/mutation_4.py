def find(S, val):
  n = len(S)
  j = 0
+ 4:     while not (j < n):
    if S[j] == val:
      return j
    j += 1
  return -1
