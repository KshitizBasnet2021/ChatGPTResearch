#mutation_21_line_no_13_ROR.py
#
#There is a bug in the provided code. The bug is in the line `llIlIlIlIlI += lIIIIlIIIIllI - min(IIlIllllIl, IlllIIIIlllIl + 1)`. 
#
#To fix the bug, we need to change the line to `llIlIlIlIlI += max(1, lIIIIlIIIIllI - min(IIlIllllIl, IlllIIIIlllIl + 1))`. 
#
#Here is the corrected code:
#
def lIIIlIIl(IIIIlIIIllllIlIlII, IllIlIIlllllllIIII):
  lIIIlIIlIIlIIl, lIIIIlIIIIllI = len(IIIIlIIIllllIlIlII), len(IllIlIIlllllllIIII)                   
  if lIIIIlIIIIllI == 0: return 0                     
  IlllllIl = {}                               
  for IIlIllllIl in range(lIIIIlIIIIllI):
    IlllllIl[ IllIlIIlllllllIIII[IIlIllllIl] ] = IIlIllllIl                      
  llIlIlIlIlI = lIIIIlIIIIllI-1                                 
  IIlIllllIl = lIIIIlIIIIllI-1                                 
  while llIlIlIlIlI < lIIIlIIlIIlIIl:
    if IIIIlIIIllllIlIlII[llIlIlIlIlI] == IllIlIIlllllllIIII[IIlIllllIl]:                      
      if IIlIllllIl != 0:
        return llIlIlIlIlI                          
      else:
        llIlIlIlIlI -= 1                            
        IIlIllllIl -= 1                            
    else:
      IlllIIIIlllIl = IlllllIl.get(IIIIlIIIllllIlIlII[llIlIlIlIlI], -1)              
      llIlIlIlIlI += max(1, lIIIIlIIIIllI - min(IIlIllllIl, IlllIIIIlllIl + 1))              
      IIlIllllIl = lIIIIlIIIIllI - 1                           
  return -1
#
#
#