#mutation_2_line_no_4_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the range of the for loop. The range should be from 0 to n - m + 1 instead of (n + m) + 1. 
#
#Here is the corrected code:
#
def find_brute(T, P):
  """Return the lowest index of T at which substring P begins (or else -1)."""
  n, m = len(T), len(P)                      # introduce convenient notations
  for i in range(n - m + 1):
    k = 0                                    # an index into pattern P
    while k < m and T[i + k] == P[k]:        # kth character of P matches
      k += 1
    if k == m:                               # if we reached the end of pattern,
      return i                               # substring T[i:i+m] matches P
  return -1                                  # failed to find a match starting with any i
#
#
#