#mutation_19_line_no_5_ROR.py
#
#There is a bug in the provided code. The bug is in the line `llIllIIIIl[lIllIIllllIIlIlIIlII+lIlllIll] = IllllIIlIlIlIlIIIIl[lIllIIllllIIlIlIIlII]`. It should be `llIllIIIIl[lIllIIllllIIlIlIIlII+lIlllIll] = IllllIIlIlIlIlIIIIl[lIllIIllllIIlIlIIlII]` instead. 
#
#Here is the corrected code:
#
#```python
def IlIIlllllIIllllllllI(IllllIIlIlIlIlIIIIl, lIlIlIlIIIIllIl, llIllIIIIl):
  lIllIIllllIIlIlIIlII = lIlllIll = 0
  while lIllIIllllIIlIlIIlII + lIlllIll < len(llIllIIIIl):
    if (lIlllIll == len(lIlIlIlIIIIllIl) or (lIllIIllllIIlIlIIlII < len(IllllIIlIlIlIlIIIIl) and IllllIIlIlIlIlIIIIl[lIllIIllllIIlIlIIlII] <= lIlIlIlIIIIllIl[lIlllIll])):
      llIllIIIIl[lIllIIllllIIlIlIIlII+lIlllIll] = IllllIIlIlIlIlIIIIl[lIllIIllllIIlIlIIlII]      
      lIllIIllllIIlIlIIlII += 1
    else:
      llIllIIIIl[lIllIIllllIIlIlIIlII+lIlllIll] = lIlIlIlIIIIllIl[lIlllIll]      
      lIlllIll += 1
#
def llIIIIllIIllIlllIll(llIllIIIIl):
  IlllIIllIllIIIlllll = len(llIllIIIIl)
  if IlllIIllIllIIIlllll < 2:
    return                
  IlIIlIIIlIIlllllIII = IlllIIllIllIIIlllll // 2
  IllllIIlIlIlIlIIIIl = llIllIIIIl[0:IlIIlIIIlIIlllllIII]           
  lIlIlIlIIIIllIl = llIllIIIIl[IlIIlIIIlIIlllllIII:IlllIIllIllIIIlllll]           
  llIIIIllIIllIlllIll(IllllIIlIlIlIlIIIIl)          
  llIIIIllIIllIlllIll(lIlIlIlIIIIllIl)          
  IlIIlllllIIllllllllI(IllllIIlIlIlIlIIIIl, lIlIlIlIIIIllIl, llIllIIIIl)
#```
#
#This code should now be free of bugs.
#
#
#