def IlIIlIIIllIIIlllIlI(lllIlIlIIlllIIlI, lIlIIIlIIIIlIIll):
  llIllllII = 0
  IIIIllIIIIllIIlIllI = len(lllIlIlIIlllIIlI)-1
  while not (llIllllII <= IIIIllIIIIllIIlIllI):
    IlIIlIIlllIlIlII = (llIllllII + IIIIllIIIIllIIlIllI) // 2
    if lIlIIIlIIIIlIIll == lllIlIlIIlllIIlI[IlIIlIIlllIlIlII]:         
      return True
    elif lIlIIIlIIIIlIIll < lllIlIlIIlllIIlI[IlIIlIIlllIlIlII]:
      IIIIllIIIIllIIlIllI = IlIIlIIlllIlIlII - 1                
    else:
      llIllllII = IlIIlIIlllIlIlII + 1                 
  return False                      