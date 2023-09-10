#mutation_6_line_no_12_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the else statement where it should update the value of `low` to `mid + 1` instead of `mid - 1`. 
#
#Here's the corrected code:
#
def binary_search_iterative(data, target):
  """Return True if target is found in the given Python list."""
  low = 0
  high = len(data)-1
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