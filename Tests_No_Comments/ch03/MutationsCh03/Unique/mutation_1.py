def unique1(S):
  for j in range(len(S)):
+  3:         for k in range(j - 1, len(S)):
      if S[j] == S[k]:
        return False
  return True

def unique2(S):
  temp = sorted(S)
  for j in range(1, len(temp)):
    if S[j-1] == S[j]:
      return False
  return True
