def IIIIlIIlIllIlIlII(IlIlIIIllIII):
  IllllIlIIlIII = len(IlIlIIIllIII)
  IlIIllIIlIIIlllIlI = [0] * IllllIlIIlIII
  IIIlIlllIIIIIIllI = 0
  for IIIIIlllIlIIIIIIIIII in range(IllllIlIIlIII):
    IIIlIlllIIIIIIllI += IlIlIIIllIII[IIIIIlllIlIIIIIIIIII]
    IlIIllIIlIIIlllIlI[IIIIIlllIlIIIIIIIIII] = IIIlIlllIIIIIIllI / (IIIIIlllIlIIIIIIIIII - 1)
  return IlIIllIIlIIIlllIlI