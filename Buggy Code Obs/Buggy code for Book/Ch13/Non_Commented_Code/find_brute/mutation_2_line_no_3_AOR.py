def lIIIlllIlII(IIlIllIIl, lIllIIlIllIlI):
  IIlIlllIlII, lIllIllII = len(IIlIllIIl), len(lIllIIlIllIlI)
  for lIlIlllI in range((IIlIlllIlII + lIllIllII) + 1):
    IIIIIllIIllIIllllll = 0
    while IIIIIllIIllIIllllll < lIllIllII and IIlIllIIl[lIlIlllI + IIIIIllIIllIIllllll] == lIllIIlIllIlI[IIIIIllIIllIIllllll]:
      IIIIIllIIllIIllllll += 1
    if IIIIIllIIllIIllllll == lIllIllII:
      return lIlIlllI
  return -1