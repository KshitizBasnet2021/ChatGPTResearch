def lIIIIlIlllIIIIllI(IlllllII, IlllIIlllIIII):
  llIIlIlIlI, IIlIlIllllIIlIlllII = len(IlllllII), len(IlllIIlllIIII)
  for IlIIIIlIIIII in range(llIIlIlIlI-IIlIlIllllIIlIlllII+1):
    IIIIIlIIlIIlIIllII = 0
    while (IIIIIlIIlIIlIIllII <= IIlIlIllllIIlIlllII and IlllllII[IlIIIIlIIIII + IIIIIlIIlIIlIIllII] == IlllIIlllIIII[IIIIIlIIlIIlIIllII]):
      IIIIIlIIlIIlIIllII += 1
    if IIIIIlIIlIIlIIllII == IIlIlIllllIIlIlllII:
      return IlIIIIlIIIII
  return -1