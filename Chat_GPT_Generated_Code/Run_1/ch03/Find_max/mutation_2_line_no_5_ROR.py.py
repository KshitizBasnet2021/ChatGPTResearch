#mutation_2_line_no_5_ROR.py
#
#Yes, there is a bug in the provided code. The condition `if val < biggest` is incorrect. It should be `if val > biggest` to find the maximum element. 
#
#Here's the corrected code:
#
def find_max(data):
  """Return the maximum element from a nonempty Python list."""
  biggest = data[0]               # The initial value to beat
  for val in data:                # For each value:
    if val > biggest:
      biggest = val               # we have found a new best (so far)
  return biggest                  # When loop ends, biggest is the max
#
#
#