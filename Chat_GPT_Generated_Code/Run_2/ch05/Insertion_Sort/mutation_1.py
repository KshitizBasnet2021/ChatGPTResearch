#mutation_1_line_no_5_AOR.py
#
#Yes, there is a bug in the provided code. In the while loop condition, it should be `A[j - 1] > cur` instead of `A[j + 1] > cur`. 
#
#Here's the corrected code:
#
def insertion_sort(A):
  for k in range(1, len(A)):
    cur = A[k]
    j = k
    while (j > 0 and A[j - 1] > cur):
      A[j] = A[j-1]
      j -= 1
    A[j] = cur
#
#Now the code should work correctly.
#
#
#