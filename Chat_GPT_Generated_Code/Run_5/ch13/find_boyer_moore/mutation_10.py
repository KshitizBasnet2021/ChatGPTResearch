#mutation_10_line_no_16_ASR.py
#
#There is a bug in the provided code. The variable `IIIIIlIlIIIl` is misspelled as `IIIIIlIlIIIl` in the line `if IIIIIlIlIIIl[lllIlIIIlIIIIIlIlI] == IIIlIIllIlIIll[lIlIIlIlllIlIl]:`. 
#
#To fix this, you can change `IIIIIlIlIIIl` to `IIIIlIlIIIl` in that line. 
#
#Here is the corrected code:
#
def IlIlllllllIllIlI(IIIIlIlIIIl, IIIlIIllIlIIll):
  llIIllIllI, IIIIIIllIIIIIl = len(IIIIlIlIIIl), len(IIIlIIllIlIIll)                   
  if IIIIIIllIIIIIl == 0: return 0                     
  llIIIIIlIlllIl = {}                               
  for lIlIIlIlllIlIl in range(IIIIIIllIIIIIl):
    llIIIIIlIlllIl[ IIIlIIllIlIIll[lIlIIlIlllIlIl] ] = lIlIIlIlllIlIl                      
  lllIlIIIlIIIIIlIlI = IIIIIIllIIIIIl-1                                 
  lIlIIlIlllIlIl = IIIIIIllIIIIIl-1                                 
  while lllIlIIIlIIIIIlIlI < llIIllIllI:
    if IIIIlIlIIIl[lllIlIIIlIIIIIlIlI] == IIIlIIllIlIIll[lIlIIlIlllIlIl]:                      
      if lIlIIlIlllIlIl == 0:
        return lllIlIIIlIIIIIlIlI                          
      else:
        lllIlIIIlIIIIIlIlI += 1
        lIlIIlIlllIlIl -= 1                            
    else:
      IIlIIIIllIl = llIIIIIlIlllIl.get(IIIIlIlIIIl[lllIlIIIlIIIIIlIlI], -1)              
      lllIlIIIlIIIIIlIlI += IIIIIIllIIIIIl - min(lIlIIlIlllIlIl, IIlIIIIllIl + 1)              
      lIlIIlIlllIlIl = IIIIIIllIIIIIl - 1                           
  return -1
#
#
#