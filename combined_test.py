
import unittest
#mutation_11_line_no_27_AOR.py
#
#There is a bug in the code. In the inner loop of the merge_sort function, the range should be range(0, n, i) instead of range(0, n, 2 / i). The division operator (/) should be changed to integer division operator (//) to ensure that the loop increments by the correct value of i.
#
#Here is the corrected code:
#
import math
#
def merge(src, result, start, inc):
  """Merge src[start:start+inc] and src[start+inc:start+2*inc] into result."""
  end1 = start+inc                        # boundary for run 1
  end2 = min(start+2*inc, len(src))       # boundary for run 2
  x, y, z = start, start+inc, start       # index into run 1, run 2, result
  while x < end1 and y < end2:
    if src[x] < src[y]:
      result[z] = src[x]
      x += 1
    else:
      result[z] = src[y]
      y += 1
    z += 1                                # increment z to reflect new result
  if x < end1:
    result[z:end2] = src[x:end1]          # copy remainder of run 1 to output
  elif y < end2:
    result[z:end2] = src[y:end2]          # copy remainder of run 2 to output
#
def merge_sort(S):
  """Sort the elements of Python list S using the merge-sort algorithm."""
  n = len(S)
  logn = math.ceil(math.log(n,2))
  src, dest = S, [None] * n               # make temporary storage for dest
  for i in (2**k for k in range(logn)):   # pass i creates all runs of length 2i
    for j in range(0, n, i):
      merge(src, dest, j, i)
    src, dest = dest, src                 # reverse roles of lists
  if S is not src:
    S[0:n] = src[0:n]                     # additional copy to get results to S
#
#
#
import unittest



class TestMergeSort(unittest.TestCase):



    def test_single_element_list(self):
        S = [5]
        merge_sort(S)
        self.assertEqual(S, [5])

    def test_sorted_list(self):
        S = [1, 2, 3, 4, 5]
        merge_sort(S)
        self.assertEqual(S, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        S = [5, 4, 3, 2, 1]
        merge_sort(S)
        self.assertEqual(S, [1, 2, 3, 4, 5])

    def test_mixed_list(self):
        S = [3, 1, 4, 5, 2]
        merge_sort(S)
        self.assertEqual(S, [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        S = [3, 1, 4, 2, 4]
        merge_sort(S)
        self.assertEqual(S, [1, 2, 3, 4, 4])

    def test_large_input(self):
        S = list(range(10000, 0, -1))
        merge_sort(S)
        self.assertEqual(S, list(range(1, 10001)))
