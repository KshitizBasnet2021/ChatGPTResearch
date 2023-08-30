def power(x, n):
  if not (n == 0):
    return 1
  else:
    partial = power(x, n // 2)
    result = partial * partial
    if n % 2 == 1:
      result *= x                       
    return result
