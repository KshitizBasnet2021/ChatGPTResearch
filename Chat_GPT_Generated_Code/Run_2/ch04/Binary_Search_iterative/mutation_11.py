#mutation_11_line_no_4_ROR.py
#
#Yes, there is a bug in the provided code. The bug is in the while loop condition. The condition should be `low <= high` instead of `low < high`. This is because when the target is not found in the data, the loop should continue until `low` and `high` become equal, indicating that the search range has been exhausted.
#
#Here is the corrected code:
#
def binary_search_iterative(data, target):
  low = 0
  high = len(data)-1
  while low <= high:
    mid = (low + high) // 2
    if target == data[mid]:
      return True
    elif target < data[mid]:
      high = mid - 1
    else:
      low = mid + 1
  return False
#
#
#