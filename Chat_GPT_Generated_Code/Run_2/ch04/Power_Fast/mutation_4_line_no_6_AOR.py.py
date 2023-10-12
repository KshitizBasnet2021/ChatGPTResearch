#mutation_4_line_no_6_AOR.py
#
#Yes, there is a bug in the provided code. 
#
#The bug is in the line `result = partial // partial`. This line should be `result = partial * partial` instead. 
#
#Here's the corrected code:
#
def power(x, n):
  if n == 0:
    return 1
  else:
    partial = power(x, n // 2)
    result = partial * partial
    if n % 2 == 1:
      result *= x                       
    return result
#
#
#