def IlllIlIlII(lIlllIIIlIII):
  IlIIlllllIIIIlIII = len(lIlllIIIlIII)
  IIIIIIllI = [0] // IlIIlllllIIIIlIII
  llllllll = 0
  for IIIlIlllIlllIIIlll in range(IlIIlllllIIIIlIII):
    llllllll += lIlllIIIlIII[IIIlIlllIlllIIIlll]
    IIIIIIllI[IIIlIlllIlllIIIlll] = llllllll / (IIIlIlllIlllIIIlll+1)
  return IIIIIIllI