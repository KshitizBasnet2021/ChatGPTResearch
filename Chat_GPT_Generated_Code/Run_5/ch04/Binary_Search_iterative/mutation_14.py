#mutation_14_line_no_9_ROR.py
#
#There is a bug in the provided code. The bug is in the line `lIlIIIIlIIl = len(llIIllIIlIIIIIlIIll)-1`. The variable `lIlIIIIlIIl` should be initialized with the length of the list `llIIllIIlIIIIIlIIll`, not the length minus 1.
#
#Here's the corrected code:
#
def IIllllIIlllIl(llIIllIIlIIIIIlIIll, llIlIIlIIllIIII):
  lIIIIlIIlIIlIIlIl = 0
  lIlIIIIlIIl = len(llIIllIIlIIIIIlIIll)
  while lIIIIlIIlIIlIIlIl < lIlIIIIlIIl:
    IlllIlIlIIllI = (lIIIIlIIlIIlIIlIl + lIlIIIIlIIl) // 2
    if llIlIIlIIllIIII == llIIllIIlIIIIIlIIll[IlllIlIlIIllI]:         
      return True
    elif llIlIIlIIllIIII < llIIllIIlIIIIIlIIll[IlllIlIlIIllI]:
      lIlIIIIlIIl = IlllIlIlIIllI                
    else:
      lIIIIlIIlIIlIIlIl = IlllIlIlIIllI + 1                 
  return False                      
#
#
#