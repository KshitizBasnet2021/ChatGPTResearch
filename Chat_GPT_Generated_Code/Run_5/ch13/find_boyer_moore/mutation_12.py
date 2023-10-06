#mutation_12_line_no_20_ASR.py
#
#There is a bug in the provided code. The bug is in the line `llIIllIlIIIllI -= llllIlllIIIlIIlIl - min(lIIIllIlllllI, lllIlIlIIlIlI + 1)`. 
#
#To fix the bug, we need to change `llllIlllIIIlIIlIl` to `lIlIllIlI` in that line. 
#
#Here is the corrected code:
#
def llIIllIIllllIl(lIIlIlIlllIIlIl, IIIlIllIlIllIlII):
  lIlIllIlI, llllIlllIIIlIIlIl = len(lIIlIlIlllIIlIl), len(IIIlIllIlIllIlII)                   
  if llllIlllIIIlIIlIl == 0: return 0                     
  lIlIllIlIllIIlI = {}                               
  for lIIIllIlllllI in range(llllIlllIIIlIIlIl):
    lIlIllIlIllIIlI[ IIIlIllIlIllIlII[lIIIllIlllllI] ] = lIIIllIlllllI                      
  llIIllIlIIIllI = llllIlllIIIlIIlIl-1                                 
  lIIIllIlllllI = llllIlllIIIlIIlIl-1                                 
  while llIIllIlIIIllI < lIlIllIlI:
    if lIIlIlIlllIIlIl[llIIllIlIIIllI] == IIIlIllIlIllIlII[lIIIllIlllllI]:                      
      if lIIIllIlllllI == 0:
        return llIIllIlIIIllI                          
      else:
        llIIllIlIIIllI -= 1                            
        lIIIllIlllllI -= 1                            
    else:
      lllIlIlIIlIlI = lIlIllIlIllIIlI.get(lIIlIlIlllIIlIl[llIIllIlIIIllI], -1)              
      llIIllIlIIIllI -= lIlIllIlI - min(lIIIllIlllllI, lllIlIlIIlIlI + 1)
      lIIIllIlllllI = lIlIllIlI - 1                           
  return -1
#
#
#