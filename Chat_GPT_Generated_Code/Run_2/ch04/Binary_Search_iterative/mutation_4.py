#mutation_4_line_no_5_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the calculation of the mid index. Instead of `(low + high) * 2`, it should be `(low + high) // 2` to find the middle index correctly.
#
#Here's the corrected code:
#
#```python
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
#```
#
#Now the code should work correctly for performing an iterative binary search.
#
#
#