#mutation_13_line_no_12_ROR.py
#
#The provided code is missing a base case for when the target is not found in the list. To fix this, we can add a return statement at the end of the function to return False if none of the conditions are met. Here's the updated code:
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
    elif target <= data[mid]:
      # recur on the portion left of the middle
      return binary_search(data, target, low, mid - 1)
    else:
      # recur on the portion right of the middle
      return binary_search(data, target, mid + 1, high)
  
  return False  # target not found in the list
#
#
#