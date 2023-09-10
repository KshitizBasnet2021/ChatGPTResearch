#mutation_3_line_no_4_ROR.py
#
#The provided code has a bug. If the input list is empty, the code will throw an IndexError because it tries to access the first element of an empty list.
#
#To fix this, we can add a check at the beginning of the function to return None if the input list is empty. Here's the updated code:
#
def find_max(data):
  if len(data) == 0:
    return None
  
  biggest = data[0]
  for val in data:
    if val >= biggest:
      biggest = val
  return biggest
#
#
#