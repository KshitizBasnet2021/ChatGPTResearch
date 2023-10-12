#mutation_13_line_no_7_ROR.py
#
#The code provided is incorrect. The condition `if n % 2 != 1` should be `if n % 2 != 0` to check if `n` is odd. 
#
#Here's the corrected code:
#
#```python
def power(x, n):
  if n == 0:
    return 1
  else:
    partial = power(x, n // 2)
    result = partial * partial
    if n % 2 != 0:
      result *= x                       
    return result
#```
#
#This code correctly calculates the power of `x` raised to `n`.
#
#
#