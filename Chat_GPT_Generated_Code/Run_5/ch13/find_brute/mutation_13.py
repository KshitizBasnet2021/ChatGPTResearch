#mutation_13_line_no_8_ROR.py
#
#There is a bug in the provided code. The variable `IIIlIllllIllIllIlI` is misspelled as `IIIlIllllIllIllIlI`. 
#
#Here's the corrected code:
#
def IIlIIIIllIIllIlIlI(llIlllIllIll, llIIIllllllllIl):
  lIIlllIlIIIIIIl, IIIlIllllIllIllIlI = len(llIlllIllIll), len(llIIIllllllllIl)                      
  for lIllllIlll in range(lIIlllIlIIIIIIl-IIIlIllllIllIllIlI+1):                     
    lIIIlIIIIlllIIIIlI = 0                                    
    while lIIIlIIIIlllIIIIlI < IIIlIllllIllIllIlI and llIlllIllIll[lIllllIlll + lIIIlIIIIlllIIIIlI] == llIIIllllllllIl[lIIIlIIIIlllIIIIlI]:        
      lIIIlIIIIlllIIIIlI += 1
    if lIIIlIIIIlllIIIIlI == IIIlIllllIllIllIlI:
      return lIllllIlll                               
  return -1
#
#
#