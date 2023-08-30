def reverse_iterative(S):
  start, stop = 0, len(S)
  while not (start < stop - 1):
    S[start], S[stop-1] = S[stop-1], S[start]
    start, stop = start + 1, stop - 1
