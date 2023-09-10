#mutation_13_line_no_7_ROR.py
#
#The provided code is missing a closing parenthesis at the end of the function definition. Here is the corrected code:
#
#```python
def find_brute(T, P):
  n, m = len(T), len(P)
  for i in range(n-m+1):
    k = 0
    while k < m and T[i + k] == P[k]:
      k += 1
    if k == m:
      return i
  return -1
#```
#
#The bug was in the condition `if k != m`, which should be `if k == m` to check if the entire pattern has been matched.
#
#
#