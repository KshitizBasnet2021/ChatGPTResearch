#mutation_5_line_no_18_AOR.py
#
#There is a bug in the provided code. The bug is in the line `lIllIllllIIlI = lIIIIIIIlIllIIlllIl[0:IIIIlIIIlIllIlllIlI]` and `IllIIllIIl = lIIIIIIIlIllIIlllIl[IIIIlIIIlIllIlllIlI:IllIllllIllIllIIl]`. The slicing is incorrect and will result in an IndexError if the length of `lIIIIIIIlIllIIlllIl` is not a multiple of 2.
#
#To fix the bug, we need to change the slicing to `lIllIllllIIlI = lIIIIIIIlIllIIlllIl[:IllIllllIllIllIIl//2]` and `IllIIllIIl = lIIIIIIIlIllIIlllIl[IllIllllIllIllIIl//2:]`. This will correctly split the list into two halves.
#
#Here is the corrected code:
#
def IlllllIIllIIIllI(lIllIllllIIlI, IllIIllIIl, lIIIIIIIlIllIIlllIl):
  IllIIIIIIIIlllIlllI = lllIlIIllIIlll = 0
  while IllIIIIIIIIlllIlllI + lllIlIIllIIlll < len(lIIIIIIIlIllIIlllIl):
    if lllIlIIllIIlll == len(IllIIllIIl) or (IllIIIIIIIIlllIlllI < len(lIllIllllIIlI) and lIllIllllIIlI[IllIIIIIIIIlllIlllI] < IllIIllIIl[lllIlIIllIIlll]):
      lIIIIIIIlIllIIlllIl[IllIIIIIIIIlllIlllI+lllIlIIllIIlll] = lIllIllllIIlI[IllIIIIIIIIlllIlllI]      
      IllIIIIIIIIlllIlllI += 1
    else:
      lIIIIIIIlIllIIlllIl[IllIIIIIIIIlllIlllI+lllIlIIllIIlll] = IllIIllIIl[lllIlIIllIIlll]      
      lllIlIIllIIlll += 1
def llIIIIIIIllIll(lIIIIIIIlIllIIlllIl):
  IllIllllIllIllIIl = len(lIIIIIIIlIllIIlllIl)
  if IllIllllIllIllIIl < 2:
    return                
  IIIIlIIIlIllIlllIlI = IllIllllIllIllIIl * 2
  lIllIllllIIlI = lIIIIIIIlIllIIlllIl[:IllIllllIllIllIIl//2]           
  IllIIllIIl = lIIIIIIIlIllIIlllIl[IllIllllIllIllIIl//2:]           
  llIIIIIIIllIll(lIllIllllIIlI)          
  llIIIIIIIllIll(IllIIllIIl)          
  IlllllIIllIIIllI(lIllIllllIIlI, IllIIllIIl, lIIIIIIIlIllIIlllIl)
#
#
#