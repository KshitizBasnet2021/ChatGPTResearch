def disjoint1(A, B, C):
  for a in A:
    for b in B:
      for c in C:
        if a == b == c:
          return False
  return True

def disjoint2(A, B, C):
  for a in A:
    for b in B:
      if a == b:
        for c in C:
         if not (a == c):
            return False
  return True
