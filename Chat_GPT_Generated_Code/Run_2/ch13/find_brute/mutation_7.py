#mutation_7_line_no_5_COI.py
#
#The provided code has a bug in the while loop condition. The condition should be `k < m` instead of `k < m and T[i + k] == P[k]`. 
#
#Here's the corrected code:
#
#```python
def find_brute(T, P):
  n, m = len(T), len(P)
  for i in range(n-m+1):
    k = 0
    while k < m:
      if T[i + k] != P[k]:
        break
      k += 1
    if k == m:
      return i
  return -1
#```
#
#In the corrected code, the while loop checks if `k` is less than `m` and breaks if the characters at the corresponding positions in `T` and `P` are not equal. This ensures that the loop terminates correctly.
#
#
#