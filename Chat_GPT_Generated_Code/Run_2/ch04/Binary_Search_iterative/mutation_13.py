#mutation_13_line_no_8_ROR.py
#
#Yes, there is a bug in the provided code. The bug is in the `elif` condition where `target > data[mid]`. The correct condition should be `target < data[mid]` to ensure that the search range is updated correctly.
#
#Here's the corrected code:
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