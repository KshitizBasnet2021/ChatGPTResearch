#mutation_3_line_no_5_ROR.py
#
#The provided code has a bug. If the input list is empty, the code will raise an IndexError when trying to access the first element (data[0]). To fix this, we can add a check at the beginning of the function to return None if the input list is empty. Here's the updated code:
#
def find_max(data):
  """Return the maximum element from a nonempty Python list."""
  if len(data) == 0:
    return None
  
  biggest = data[0]               # The initial value to beat
  for val in data:                # For each value:
    if val >= biggest:
      biggest = val               # we have found a new best (so far)
  return biggest                  # When loop ends, biggest is the max
#
#
#