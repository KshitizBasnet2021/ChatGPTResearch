#mutation_2_line_no_4_AOR.py
#
#The provided code is an implementation of the string matching algorithm known as the "Naive String Matching" algorithm. It searches for a pattern within a text and returns the index of the first occurrence of the pattern in the text.
#
#There are no syntax errors in the code, but there is a logical error in the while loop condition. The loop should terminate when either the pattern is fully matched or when the end of the text is reached. However, the current condition only checks if the pattern is fully matched. To fix this, we need to add an additional condition to check if the end of the text is reached.
#
#Here's the corrected code:
#
def IlIlIIllIllllIIIlIll(IlIIllIllIl, lIIlIllIIIIlIIIl):
  llIIlIIl, lIIIlIlIlllIIlI = len(IlIIllIllIl), len(lIIlIllIIIIlIIIl)                      
  for lIIIIIlIlIlllllll in range((llIIlIIl + lIIIlIlIlllIIlI) + 1):
    lIIlIIlIlIIlIlIIl = 0                                    
    while lIIlIIlIlIIlIlIIl < lIIIlIlIlllIIlI and lIIIIIlIlIlllllll + lIIlIIlIlIIlIlIIl < llIIlIIl and IlIIllIllIl[lIIIIIlIlIlllllll + lIIlIIlIlIIlIlIIl] == lIIlIllIIIIlIIIl[lIIlIIlIlIIlIlIIl]:        
      lIIlIIlIlIIlIlIIl += 1
    if lIIlIIlIlIIlIlIIl == lIIIlIlIlllIIlI:                               
      return lIIIIIlIlIlllllll                               
  return -1
#
#Now, the while loop condition checks if both the pattern is not fully matched and the end of the text is not reached.
#
#
#