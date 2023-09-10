#mutation_7_line_no_6_COI.py
#
#The provided code has a bug. The while loop condition should be modified to check if k is less than m and if T[i + k] is equal to P[k]. Currently, the condition is checking if k is less than m and if T[i + k] is not equal to P[k]. 
#
#Here's the corrected code:
#
def find_brute(T, P):
  """Return the lowest index of T at which substring P begins (or else -1)."""
  n, m = len(T), len(P)                      # introduce convenient notations
  for i in range(n-m+1):                     # try every potential starting index within T
    k = 0                                    # an index into pattern P
    while k < m and T[i + k] == P[k]:
      k += 1
    if k == m:                               # if we reached the end of pattern,
      return i                               # substring T[i:i+m] matches P
  return -1                                  # failed to find a match starting with any i
#
#
#