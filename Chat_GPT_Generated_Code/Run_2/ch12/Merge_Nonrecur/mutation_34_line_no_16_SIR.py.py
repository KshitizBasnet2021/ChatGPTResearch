#mutation_34_line_no_16_SIR.py
#
#There is a bug in the provided code. In the merge_sort function, the line "if S is not src:" should be changed to "if S is not dest:". This is because after the sorting is complete, the sorted elements are stored in the 'dest' list, so we need to check if 'S' is not equal to 'dest' to determine if we need to copy the sorted elements back to 'S'. 
#
#Here is the corrected code:
#
import math
#
def merge(src, result, start, inc):
  end1 = start+inc
  end2 = min(start+2*inc, len(src))
  x, y, z = start, start+inc, start
  while x < end1 and y < end2:
    if src[x] < src[y]:
      result[z] = src[x]
      x += 1
    else:
      result[z] = src[y]
      y += 1
    z += 1
  if x < end1:
    result[z:] = src[x:end1]
  elif y < end2:
    result[z:end2] = src[y:end2]
#
def merge_sort(S):
  n = len(S)
  logn = math.ceil(math.log(n,2))
  src, dest = S, [None] * n
  for i in (2**k for k in range(logn)):
    for j in range(0, n, 2*i):
      merge(src, dest, j, i)
    src, dest = dest, src
  if S is not dest:
    S[0:n] = dest[0:n]
#
#
#