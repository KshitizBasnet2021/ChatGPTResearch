def unique1(S):
  """Return True if there are no duplicate elements in sequence S."""
  for j in range(len(S)):
    for k in range(j+1, len(S)):
      if not (S[j] == S[k]):
        return False              # found duplicate pair
  return True                     # if we reach this, elements were unique
