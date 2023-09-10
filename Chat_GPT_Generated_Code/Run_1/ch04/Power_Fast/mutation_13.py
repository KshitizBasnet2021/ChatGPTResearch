#mutation_13_line_no_8_ROR.py
#
#The provided code is missing a base case for when n is negative. To fix this, we can add a condition to check if n is less than 0 and return 1 divided by the result of power(x, -n). This will handle negative exponents correctly.
#
#Here's the updated code:
#
def power(x, n):
  """Compute the value x**n for integer n."""
  if n == 0:
    return 1
  elif n < 0:
    return 1 / power(x, -n)
  else:
    partial = power(x, n // 2)          # rely on truncated division
    result = partial * partial
    if n % 2 != 1:
      result *= x                       
    return result
#
#
#