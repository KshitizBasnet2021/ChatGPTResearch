#mutation_5_line_no_10_AOR.py
#
#Yes, there is a bug in the provided code. In the line `high = mid + 1` inside the `elif` statement, it should be `high = mid - 1` instead. This is because if the target is less than the value at the middle index, we should update the `high` index to be one less than the middle index, not one more.
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
    elif target < data[mid]:
      high = mid - 1
    else:
      low = mid + 1                 # only consider values right of mid
  return False                      # loop ended without success
#
#
#