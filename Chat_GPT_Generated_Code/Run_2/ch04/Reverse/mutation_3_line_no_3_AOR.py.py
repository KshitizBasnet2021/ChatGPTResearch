#mutation_3_line_no_3_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the line where the swap is happening:
#
#(S[start], S[stop - 1]) = (S[stop + 1], S[start])
#
#The indices used for swapping are incorrect. It should be:
#
#(S[start], S[stop - 1]) = (S[stop - 1], S[start])
#
#Here's the corrected code:
#
def reverse(S, start, stop):
  if start < stop - 1:
    (S[start], S[stop - 1]) = (S[stop - 1], S[start])
    reverse(S, start+1, stop-1)
#
#
#