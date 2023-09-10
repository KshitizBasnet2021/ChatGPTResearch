#mutation_10_line_no_2_COI.py
#
#Yes, there is a bug in the provided code. The bug is in the first line of the code where it checks if n is not equal to 0. It should be checking if n is equal to 0 instead. 
#
#Here is the corrected code:
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