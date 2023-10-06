#mutation_18_line_no_11_ROR.py
#
#There is a bug in the provided code. The while loop condition should be `while IlIlIlIlllIIIlIl >= IlIllIllIllllIIIll:` instead of `while IlIlIlIlllIIIlIl > IlIllIllIllllIIIll:`. This is because the loop should continue until `IlIlIlIlllIIIlIl` is greater than or equal to `IlIllIllIllllIIIll`, not just greater than `IlIllIllIllllIIIll`.
#
#Here is the corrected code:
#
def lllIIllIIIllIlll(lIlllIIlIllll, IllIlIIlIlIIllIIIl):
  IlIllIllIllllIIIll, IlIIIIlIllIIlIIIlll = len(lIlllIIlIllll), len(IllIlIIlIlIIllIIIl)                   
  if IlIIIIlIllIIlIIIlll == 0: return 0                     
  IlIIlIlllIlllIIIlII = {}                               
  for IllIIlllllIIIlIllIl in range(IlIIIIlIllIIlIIIlll):
    IlIIlIlllIlllIIIlII[ IllIlIIlIlIIllIIIl[IllIIlllllIIIlIllIl] ] = IllIIlllllIIIlIllIl                      
  IlIlIlIlllIIIlIl = IlIIIIlIllIIlIIIlll-1                                 
  IllIIlllllIIIlIllIl = IlIIIIlIllIIlIIIlll-1                                 
  while IlIlIlIlllIIIlIl >= IlIllIllIllllIIIll:
    if lIlllIIlIllll[IlIlIlIlllIIIlIl] == IllIlIIlIlIIllIIIl[IllIIlllllIIIlIllIl]:                      
      if IllIIlllllIIIlIllIl == 0:
        return IlIlIlIlllIIIlIl                          
      else:
        IlIlIlIlllIIIlIl -= 1                            
        IllIIlllllIIIlIllIl -= 1                            
    else:
      IIlllIII = IlIIlIlllIlllIIIlII.get(lIlllIIlIllll[IlIlIlIlllIIIlIl], -1)              
      IlIlIlIlllIIIlIl += IlIIIIlIllIIlIIIlll - min(IllIIlllllIIIlIllIl, IIlllIII + 1)              
      IllIIlllllIIIlIllIl = IlIIIIlIllIIlIIIlll - 1                           
  return -1
#
#
#