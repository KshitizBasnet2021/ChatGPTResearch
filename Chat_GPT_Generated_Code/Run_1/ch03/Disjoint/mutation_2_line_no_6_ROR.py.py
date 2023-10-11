#mutation_2_line_no_6_ROR.py
#
#Yes, there is a bug in the provided code. The condition `if a != b == c` is incorrect. It should be `if a == b == c` to check if all three elements are equal. 
#
#Here's the corrected code:
#
def disjoint1(A, B, C):
  """Return True if there is no element common to all three lists."""
  for a in A:
    for b in B:
      for c in C:
        if a == b == c:
          return False      # we found a common value
  return True               # if we reach this, sets are disjoint
#
#
#