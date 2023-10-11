#mutation_6_line_no_6_ROR.py
#
#Yes, there is a bug in the provided code. The condition in the while loop should be `while (j > 0 and A[j - 1] > cur)` instead of `while (j < 0 and A[j - 1] > cur)`. 
#
#Here's the corrected code:
#
def insertion_sort(A):
  """Sort list of comparable elements into nondecreasing order."""
  for k in range(1, len(A)):         # from 1 to n-1
    cur = A[k]                       # current element to be inserted
    j = k                            # find correct index j for current
    while (j > 0 and A[j - 1] > cur):
      A[j] = A[j-1]
      j -= 1
    A[j] = cur                       # cur is now in the right place
#
#
#