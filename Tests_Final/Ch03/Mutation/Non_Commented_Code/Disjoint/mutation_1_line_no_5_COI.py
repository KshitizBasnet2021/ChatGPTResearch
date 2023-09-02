def disjoint1(A, B, C):
  for a in A:
    for b in B:
      for c in C:
        if not (a == b == c):
          return False
  return True