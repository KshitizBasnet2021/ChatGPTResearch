#mutation_18_line_no_10_ROR.py
#
#Yes, there are a few bugs in the provided code. Here's the fixed code:
#
#```python
def find_boyer_moore(T, P):
  n, m = len(T), len(P)
  if m == 0: return 0
  last = {}
  for k in range(m):
    last[ P[k] ] = k
  i = m-1
  k = m-1
  while i < n:
    while i >= 0:
      if T[i] == P[k]:
        if k == 0:
          return i
        else:
          i -= 1
          k -= 1
      else:
        break
    j = last.get(T[i+m], -1)
    i += m - min(k, j + 1)
    k = m - 1
  return -1
#```
#
#Here are the changes made:
#
#1. In the inner while loop, the condition `while i > n` should be `while i >= 0` to ensure that we iterate over the characters of the text string correctly.
#2. Inside the inner while loop, we need to check if the current characters match (`T[i] == P[k]`). If they do, we continue decrementing `i` and `k`. If they don't match, we break out of the loop.
#3. In the line `j = last.get(T[i], -1)`, we need to check `T[i+m]` instead of `T[i]` to get the last occurrence of the character in the pattern.
#4. Finally, we return -1 if no match is found.
#
#With these fixes, the code should work correctly.
#
#
#