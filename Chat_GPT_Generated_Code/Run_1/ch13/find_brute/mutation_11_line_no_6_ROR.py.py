#mutation_11_line_no_6_ROR.py
#
#Yes, there is a bug in the provided code. The condition in the while loop should be `k < m` instead of `k <= m`. This is because the index `k` should be less than the length of pattern `m` in order to access the elements of pattern `P`. 
#
#Here is the corrected code:
#
def find_brute(T, P):
  """Return the lowest index of T at which substring P begins (or else -1)."""
  n, m = len(T), len(P)                      # introduce convenient notations
  for i in range(n-m+1):                     # try every potential starting index within T
    k = 0                                    # an index into pattern P
    while (k < m and T[i + k] == P[k]):
      k += 1
    if k == m:                               # if we reached the end of pattern,
      return i                               # substring T[i:i+m] matches P
  return -1                                  # failed to find a match starting with any i
#
#
#