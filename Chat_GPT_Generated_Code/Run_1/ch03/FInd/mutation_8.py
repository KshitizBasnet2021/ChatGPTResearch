#mutation_8_line_no_6_ROR.py
#
#The provided code has a bug. The return statement inside the while loop should be outside the loop, after the loop has finished iterating through all the elements of the list. Here's the corrected code:
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