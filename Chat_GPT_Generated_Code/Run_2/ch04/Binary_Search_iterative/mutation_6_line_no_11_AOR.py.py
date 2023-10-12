#mutation_6_line_no_11_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the else statement where it should update the value of `low` to `mid + 1` instead of `mid - 1`. 
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