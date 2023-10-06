#mutation_2_line_no_9_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the return statement at the end of the function. The code is returning +1 instead of returning -1 when the element is not found in the list.
#
#Here's the corrected code:
#
def IIlIlIlIlllIII(llIIIIIIIlIIIIlIll, IlllIIIlIIlIlIl):
  IIIlIIlII = len(llIIIIIIIlIIIIlIll)
  lIIlIIIIIlIIllI = 0
  while lIIlIIIIIlIIllI < IIIlIIlII:
    if llIIIIIIIlIIIIlIll[lIIlIIIIIlIIllI] == IlllIIIlIIlIlIl:
      return lIIlIIIIIlIIllI          
    lIIlIIIIIlIIllI += 1
  return -1
#
#Now, the function will return -1 if the element is not found in the list.
#
#
#