#mutation_2_line_no_6_AOR.py
#
#There is a bug in the provided code. The line `llllIIlIIllIIlI = (lIllllIIlIlIII - IIlIlIlIIIllIlIII) // 2` should be `llllIIlIIllIIlI = (lIllllIIlIlIII + IIlIlIlIIIllIlIII) // 2`. 
#
#Here is the corrected code:
#
def IIlIIllllIIIIllIl(lIIlllIII, IIlIIlllIlIIIIl):
  lIllllIIlIlIII = 0
  IIlIlIlIIIllIlIII = len(lIIlllIII)-1
  while lIllllIIlIlIII <= IIlIlIlIIIllIlIII:
    llllIIlIIllIIlI = (lIllllIIlIlIII + IIlIlIlIIIllIlIII) // 2
    if IIlIIlllIlIIIIl == lIIlllIII[llllIIlIIllIIlI]:         
      return True
    elif IIlIIlllIlIIIIl < lIIlllIII[llllIIlIIllIIlI]:
      IIlIlIlIIIllIlIII = llllIIlIIllIIlI - 1                
    else:
      lIllllIIlIlIII = llllIIlIIllIIlI + 1                 
  return False
#
#
#