def power(x, n):
  """Compute the value x**n for integer n."""
  if n == 0:
    return 1
  else:
    partial = power(x, n // 2)          # rely on truncated division
    result = partial * partial
    if not (n % 2 == 1):
      result *= x                       
    return result
