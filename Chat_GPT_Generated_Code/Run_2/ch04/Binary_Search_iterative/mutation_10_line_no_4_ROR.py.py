#mutation_10_line_no_4_ROR.py
#
#Yes, there is a bug in the provided code. The condition in the while loop is incorrect. It should be `low <= high` instead of `low >= high`. 
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