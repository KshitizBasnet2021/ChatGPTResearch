#mutation_12_line_no_5_ROR.py
#
#The provided code is a brute force algorithm for finding a pattern in a text. It searches for the pattern P in the text T and returns the index of the first occurrence of P in T. If the pattern is not found, it returns -1.
#
#The code looks correct and there are no apparent bugs. However, there is one improvement that can be made to optimize the algorithm.
#
#Currently, the code uses a nested loop to compare each character of the pattern P with the corresponding character in the text T. This results in a time complexity of O(n * m), where n is the length of the text and m is the length of the pattern.
#
#To optimize the algorithm, we can use the "early exit" strategy. Instead of comparing each character of the pattern with the text, we can compare the entire pattern with a substring of the text. If the substring does not match the pattern, we can skip to the next substring without comparing individual characters.
#
#Here's the updated code with the optimization:
#
def find_brute(T, P):
  n, m = len(T), len(P)
  for i in range(n-m+1):
    if T[i:i+m] == P:
      return i
  return -1
#
#With this optimization, the time complexity of the algorithm is reduced to O(n), where n is the length of the text.
#
#
#