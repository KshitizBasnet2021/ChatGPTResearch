#mutation_2_line_no_6_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the line where the midpoint is calculated:
#
#mid = (low + high) / 2
#
#In Python 3, the division operator (/) performs floating-point division, which can result in a float value. However, the binary_search function expects the midpoint to be an integer index.
#
#To fix this bug, we can use the integer division operator (//) instead of the division operator (/) to ensure that the midpoint is always an integer:
#
#mid = (low + high) // 2
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