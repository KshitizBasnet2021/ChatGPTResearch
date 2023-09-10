#mutation_12_line_no_6_ROR.py
#
#The provided code is missing a colon at the end of the function definition. Here is the corrected code:
#
#```python
def find_brute(T, P):
  """Return the lowest index of T at which substring P begins (or else -1)."""
  n, m = len(T), len(P)                      # introduce convenient notations
  for i in range(n-m+1):                     # try every potential starting index within T
    k = 0                                    # an index into pattern P
    while (k < m and T[i + k] != P[k]):
      k += 1
    if k == m:                               # if we reached the end of pattern,
      return i                               # substring T[i:i+m] matches P
  return -1                                  # failed to find a match starting with any i
#```
#
#The code should now be free of syntax errors.
#
#
#