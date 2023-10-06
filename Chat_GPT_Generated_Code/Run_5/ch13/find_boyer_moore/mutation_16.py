#mutation_16_line_no_13_COI.py
#
#There is a bug in the provided code. The bug is in the line `lIllIlIlIlIlI += llIIlIlIIlIlIlIIlI - min(IlIIlllIllIIll, IlllIIlIIIlIIIII + 1)`. 
#
#To fix the bug, we need to change the line to `lIllIlIlIlIlI += llIIlIlIIlIlIlIIlI - min(IlIIlllIllIIll, IlllIIlIIIlIIIII + 1) - 1`. 
#
#Here is the corrected code:
#
#```python
def IIllIIllIII(IllIIlIIIlIlIIlIlIl, IlIIIllIIlIIlIIIIIl):
  llIlIIllllIlIIIlIl, llIIlIlIIlIlIlIIlI = len(IllIIlIIIlIlIIlIlIl), len(IlIIIllIIlIIlIIIIIl)                   
  if llIIlIlIIlIlIlIIlI == 0: return 0                     
  IlIlIlIll = {}                               
  for IlIIlllIllIIll in range(llIIlIlIIlIlIlIIlI):
    IlIlIlIll[ IlIIIllIIlIIlIIIIIl[IlIIlllIllIIll] ] = IlIIlllIllIIll                      
  lIllIlIlIlIlI = llIIlIlIIlIlIlIIlI-1                                 
  IlIIlllIllIIll = llIIlIlIIlIlIlIIlI-1                                 
  while lIllIlIlIlIlI < llIlIIllllIlIIIlIl:
    if IllIIlIIIlIlIIlIlIl[lIllIlIlIlIlI] == IlIIIllIIlIIlIIIIIl[IlIIlllIllIIll]:                      
      if not (IlIIlllIllIIll == 0):
        return lIllIlIlIlIlI                          
      else:
        lIllIlIlIlIlI -= 1                            
        IlIIlllIllIIll -= 1                            
    else:
      IlllIIlIIIlIIIII = IlIlIlIll.get(IllIIlIIIlIlIIlIlIl[lIllIlIlIlIlI], -1)              
      lIllIlIlIlIlI += llIIlIlIIlIlIlIIlI - min(IlIIlllIllIIll, IlllIIlIIIlIIIII + 1) - 1              
      IlIIlllIllIIll = llIIlIlIIlIlIlIIlI - 1                           
  return -1
#```
#
#
#