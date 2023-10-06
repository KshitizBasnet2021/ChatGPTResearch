#mutation_6_line_no_3_COI.py
#
#There is a bug in the provided code. The bug is in the line `return IllllIIlIIIIIlIlllII(llIllIllllIIllI, IIlIIlllIIlIIl, IlIlIIIlIIIlIIlIIll)`. The second recursive call should have the arguments `IIlIIlllIIlIIl, IlIlIIIlIIIlIIlIIll` instead of `llIllIllllIIllI, IIlIIlllIIlIIl, IlIlIIIlIIIlIIlIIll`. 
#
#Here is the corrected code:
#
def IllllIIlIIIIIlIlllII(llIllIllllIIllI, lIlllIIllIllIlllI, IlIlIIIlIIIlIIlIIll):
  if not (lIlllIIllIllIlllI >= IlIlIIIlIIIlIIlIIll):
    return 0
  elif lIlllIIllIllIlllI == IlIlIIIlIIIlIIlIIll-1:                  
    return llIllIllllIIllI[lIlllIIllIllIlllI]
  else:                                  
    IIlIIlllIIlIIl = (lIlllIIllIllIlllI + IlIlIIIlIIIlIIlIIll) // 2
    return IllllIIlIIIIIlIlllII(llIllIllllIIllI, lIlllIIllIllIlllI, IIlIIlllIIlIIl) + IllllIIlIIIIIlIlllII(llIllIllllIIllI, IIlIIlllIIlIIl, IlIlIIIlIIIlIIlIIll)
#
#
#