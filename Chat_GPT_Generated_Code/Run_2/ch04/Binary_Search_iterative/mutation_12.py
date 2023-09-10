#mutation_12_line_no_6_ROR.py
#
#Yes, there is a bug in the provided code. The bug is in the line `if target != data[mid]:`. This condition should be checking if the target is equal to `data[mid]` instead of not equal to `data[mid]`. 
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