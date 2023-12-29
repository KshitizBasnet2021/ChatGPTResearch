def unique1(S):
  """Return True if there are no duplicate elements in sequence S."""
  if len(S) == 0:
    return True

  for j in range(len(S)):
    for k in range(j+1, len(S)):
      if S[j] == S[k]:
        return False              # found duplicate pair
  return True                     # if we reach this, elements were unique