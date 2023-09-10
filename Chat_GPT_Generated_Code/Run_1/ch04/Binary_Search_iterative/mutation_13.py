#mutation_13_line_no_9_ROR.py
#
#Yes, there is a bug in the provided code. The bug is in the lines where the values of `high` and `low` are updated.
#
#To fix the bug, we need to update the values of `high` and `low` correctly. 
#
#Here is the corrected code:
#
def binary_search_iterative(data, target):
  """Return True if target is found in the given Python list."""
  low = 0
  high = len(data)-1
  while low <= high:
    mid = (low + high) // 2
    if target == data[mid]:         # found a match
      return True
    elif target > data[mid]:
      low = mid + 1                 # only consider values right of mid
    else:
      high = mid - 1                # only consider values left of mid
  return False                      # loop ended without success
#
#
#