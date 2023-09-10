#mutation_1_line_no_4_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the initialization of the `high` variable. It should be initialized to `len(data) - 1` instead of `len(data) + 1`. 
#
#Here's the corrected code:
#
def binary_search_iterative(data, target):
  """Return True if target is found in the given Python list."""
  low = 0
  high = len(data) - 1
  while low <= high:
    mid = (low + high) // 2
    if target == data[mid]:         # found a match
      return True
    elif target < data[mid]:
      high = mid - 1                # only consider values left of mid
    else:
      low = mid + 1                 # only consider values right of mid
  return False                      # loop ended without success
#
#
#