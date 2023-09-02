def unique1(S):
  for j in range(len(S)):
    for k in range(j+1, len(S)):
      if S[j] != S[k]:
        return False
  return True
