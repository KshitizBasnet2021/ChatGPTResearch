#mutation_5_line_no_6_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the line `result = partial ** partial`. It should be `result = partial ** 2` instead. 
#
#Here's the corrected code:
#
def power(x, n):
  if n == 0:
    return 1
  else:
    partial = power(x, n // 2)
    result = partial ** 2
    if n % 2 == 1:
      result *= x                       
    return result
#
#
#