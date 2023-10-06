#mutation_11_line_no_5_LCR.py
#
#There is a bug in the provided code. The bug is in the line `if (IIIlIllllllIl == len(IlllllllI) and (IlIlIIlIl < len(llIIlIIIlIII) and llIIlIIIlIII[IlIlIIlIl] < IlllllllI[IIIlIllllllIl])):`. The condition should be `if (IIIlIllllllIl == len(IlllllllI) or (IlIlIIlIl < len(llIIlIIIlIII) and llIIlIIIlIII[IlIlIIlIl] < IlllllllI[IIIlIllllllIl])):`. 
#
#Here's the corrected code:
#
def lIlIIlIlIIIlll(llIIlIIIlIII, IlllllllI, IIIIIlllIIIlllllll):
  IlIlIIlIl = IIIlIllllllIl = 0
  while IlIlIIlIl + IIIlIllllllIl < len(IIIIIlllIIIlllllll):
    if (IIIlIllllllIl == len(IlllllllI) or (IlIlIIlIl < len(llIIlIIIlIII) and llIIlIIIlIII[IlIlIIlIl] < IlllllllI[IIIlIllllllIl])):
      IIIIIlllIIIlllllll[IlIlIIlIl+IIIlIllllllIl] = llIIlIIIlIII[IlIlIIlIl]      
      IlIlIIlIl += 1
    else:
      IIIIIlllIIIlllllll[IlIlIIlIl+IIIlIllllllIl] = IlllllllI[IIIlIllllllIl]      
      IIIlIllllllIl += 1
#
def lllllIIlllIlIlIllll(IIIIIlllIIIlllllll):
  lIlllllI = len(IIIIIlllIIIlllllll)
  if lIlllllI < 2:
    return                
  IllIIIIIIll = lIlllllI // 2
  llIIlIIIlIII = IIIIIlllIIIlllllll[0:IllIIIIIIll]           
  IlllllllI = IIIIIlllIIIlllllll[IllIIIIIIll:lIlllllI]           
  lllllIIlllIlIlIllll(llIIlIIIlIII)          
  lllllIIlllIlIlIllll(IlllllllI)          
  lIlIIlIlIIIlll(llIIlIIIlIII, IlllllllI, IIIIIlllIIIlllllll)
#
#
#