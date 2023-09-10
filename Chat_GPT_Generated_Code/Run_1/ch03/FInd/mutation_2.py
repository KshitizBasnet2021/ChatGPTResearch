#mutation_2_line_no_9_AOR.py
#
#Yes, there is a bug in the provided code. The return statement at the end of the function should return -1 instead of +1. Here's the corrected code:
#
def find(S, val):
  """Return index j such that S[j] == val, or -1 if no such element."""
  n = len(S)
  j = 0
  while j < n:
    if S[j] == val:
      return j          # a match was found at index j
    j += 1
  return -1
#
#
#