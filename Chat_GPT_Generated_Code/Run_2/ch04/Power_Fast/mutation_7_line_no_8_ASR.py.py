#mutation_7_line_no_8_ASR.py
#
#The code provided has a bug when dividing the result by x if n is odd. Since the division operator (/) returns a float, it can introduce floating-point precision errors. To fix this, we can use the integer division operator (//) instead.
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
      result //= x
    return result
#
#
#