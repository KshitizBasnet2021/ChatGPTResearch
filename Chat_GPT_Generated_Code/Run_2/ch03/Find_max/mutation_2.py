#mutation_2_line_no_4_ROR.py
#
#Yes, there is a bug in the provided code. The bug is in the comparison condition inside the for loop. The condition should be `if val > biggest` instead of `if val < biggest`. 
#
#Here's the corrected code:
#
def find_max(data):
  biggest = data[0]
  for val in data:
    if val > biggest:
      biggest = val
  return biggest
#
#
#