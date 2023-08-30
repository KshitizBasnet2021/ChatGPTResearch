def disjoint1(A, B, C):
  """Return True if there is no element common to all three lists."""
  for a in A:
    for b in B:
      for c in C:
        if a == b == c:
          return False      # we found a common value
  return True               # if we reach this, sets are disjoint

def disjoint2(A, B, C):
  """Return True if there is no element common to all three lists."""
  for a in A:
    for b in B:
      if not (a == b):
        for c in C:
          if a == c:        # (and thus a == b == c)
            return False    # we found a common value
  return True               # if we reach this, sets are disjoint
