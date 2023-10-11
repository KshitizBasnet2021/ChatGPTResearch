#mutation_9_line_no_6_ROR.py
#
#Yes, there is a bug in the provided code. The bug is in the condition `if low < high:`. It should be `if low <= high:` instead. 
#
#Here's the corrected code:
#
def binary_search(data, target, low, high):
  """Return True if target is found in indicated portion of a Python list.
#
  The search only considers the portion from data[low] to data[high] inclusive.
  """
  if low > high:
    return False                    # interval is empty; no match
  else:
    mid = (low + high) // 2
    if target == data[mid]:         # found a match
      return True
    elif target < data[mid]:
      # recur on the portion left of the middle
      return binary_search(data, target, low, mid - 1)
    else:
      # recur on the portion right of the middle
      return binary_search(data, target, mid + 1, high)
#
#
#