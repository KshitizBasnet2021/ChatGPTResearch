def lIIIIIlIIlIIIlllIII(lIIlIlIlIIIIlIIlIlII, IIIllIIlIllllIII):
  IlIIIlIIlllllIIllI, lIIIlIlIllIIIllIlII = len(lIIlIlIlIIIIlIIlIlII), len(IIIllIIlIllllIII)
  for IIlllIII in range(IlIIIlIIlllllIIllI-lIIIlIlIllIIIllIlII+1):
    IlIIIllIIIIIlII = 0
    while (IlIIIllIIIIIlII < lIIIlIlIllIIIllIlII and lIIlIlIlIIIIlIIlIlII[IIlllIII + IlIIIllIIIIIlII] != IIIllIIlIllllIII[IlIIIllIIIIIlII]):
      IlIIIllIIIIIlII += 1
    if IlIIIllIIIIIlII == lIIIlIlIllIIIllIlII:
      return IIlllIII
  return -1