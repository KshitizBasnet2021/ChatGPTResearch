#mutation_5_line_no_6_LCR.py
#
#Yes, there is a bug in the provided code. The condition in the while loop should be "j > 0 and A[j - 1] > cur" instead of "j > 0 or A[j - 1] > cur". 
#
#Here is the corrected code:
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