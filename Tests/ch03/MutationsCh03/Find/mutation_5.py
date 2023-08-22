def find(S, val):
  """Return index j such that S[j] == val, or -1 if no such element."""
  n = len(S)
  j = 0
  while j < n:
    if not (S[j] == val):  #     if S[j] == val:
      return j          # a match was found at index j
    j += 1
  return -1
