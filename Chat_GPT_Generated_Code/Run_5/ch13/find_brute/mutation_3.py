#mutation_3_line_no_4_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the range of the for loop. The range should be (lIlIlllIIll - IIIIIIIIlI + 1) instead of (lIlIlllIIll - IIIIIIIIlI) - 1. 
#
#Here is the corrected code:
#
def IIIIlIIllIIlIIlIIIII(lIIIIIIllll, IlIlllIllII):
  lIlIlllIIll, IIIIIIIIlI = len(lIIIIIIllll), len(IlIlllIllII)                      
  for llIIIIlIlIlIIlllllll in range((lIlIlllIIll - IIIIIIIIlI + 1)):
    lIllllIlIIIIlllI = 0                                    
    while lIllllIlIIIIlllI < IIIIIIIIlI and lIIIIIIllll[llIIIIlIlIlIIlllllll + lIllllIlIIIIlllI] == IlIlllIllII[lIllllIlIIIIlllI]:        
      lIllllIlIIIIlllI += 1
    if lIllllIlIIIIlllI == IIIIIIIIlI:                               
      return llIIIIlIlIlIIlllllll                               
  return -1
#
#
#