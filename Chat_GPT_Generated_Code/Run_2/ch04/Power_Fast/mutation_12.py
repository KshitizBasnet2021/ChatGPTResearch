#mutation_12_line_no_2_ROR.py
#
#Yes, there is a bug in the provided code. The condition in the if statement is incorrect. It should be `if n == 0:` instead of `if n != 0:`. 
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