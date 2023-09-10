#mutation_10_line_no_3_ROR.py
#
#Yes, there is a bug in the provided code. The condition `if low >= high` should be `if low > high` in order to correctly handle the case when the target is not found in the data.
#
#Here is the corrected code:
#
def binary_search(data, target, low, high):
  if low > high:
    return False
  else:
    mid = (low + high) // 2
    if target == data[mid]:
      return True
    elif target < data[mid]:
      return binary_search(data, target, low, mid - 1)
    else:
      return binary_search(data, target, mid + 1, high)
#
#
#