#mutation_4_line_no_5_COI.py
#
#The provided code is a simple implementation of the linear search algorithm to find the index of an element in a list. However, there is a bug in the code. The bug is in the while loop condition. The condition should be "lIlllllIIIlI < lIllIIIIlIII" instead of "not (lIlllllIIIlI < lIllIIIIlIII)". 
#
#Here is the corrected code:
#
def lIlIllIIllIl(llIlIIIIIlllIIIllI, lIlIlllIIIl):
  lIllIIIIlIII = len(llIlIIIIIlllIIIllI)
  lIlllllIIIlI = 0
  while lIlllllIIIlI < lIllIIIIlIII:
    if llIlIIIIIlllIIIllI[lIlllllIIIlI] == lIlIlllIIIl:
      return lIlllllIIIlI          
    lIlllllIIIlI += 1
  return -1
#
#Now the code should work correctly.
#
#
#