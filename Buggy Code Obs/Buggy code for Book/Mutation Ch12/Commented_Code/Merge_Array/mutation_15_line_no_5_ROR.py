def lIlIlIIlIllIIIIIII(IIllllllllIIII, lIIlIIIIllI, lIIlllll):
  IIIIllIllIIIllIIll = IIllIllI = 0
  while IIIIllIllIIIllIIll + IIllIllI < len(lIIlllll):
    if (IIllIllI != len(lIIlIIIIllI) or (IIIIllIllIIIllIIll < len(IIllllllllIIII) and IIllllllllIIII[IIIIllIllIIIllIIll] < lIIlIIIIllI[IIllIllI])):
      lIIlllll[IIIIllIllIIIllIIll+IIllIllI] = IIllllllllIIII[IIIIllIllIIIllIIll]      
      IIIIllIllIIIllIIll += 1
    else:
      lIIlllll[IIIIllIllIIIllIIll+IIllIllI] = lIIlIIIIllI[IIllIllI]      
      IIllIllI += 1
def IllIIllIIIlIlIlIlllI(lIIlllll):
  IllIIIIIlIlII = len(lIIlllll)
  if IllIIIIIlIlII < 2:
    return                
  lIllIlIIIIIlIIIllII = IllIIIIIlIlII // 2
  IIllllllllIIII = lIIlllll[0:lIllIlIIIIIlIIIllII]           
  lIIlIIIIllI = lIIlllll[lIllIlIIIIIlIIIllII:IllIIIIIlIlII]           
  IllIIllIIIlIlIlIlllI(IIllllllllIIII)          
  IllIIllIIIlIlIlIlllI(lIIlIIIIllI)          
  lIlIlIIlIllIIIIIII(IIllllllllIIII, lIIlIIIIllI, lIIlllll)        