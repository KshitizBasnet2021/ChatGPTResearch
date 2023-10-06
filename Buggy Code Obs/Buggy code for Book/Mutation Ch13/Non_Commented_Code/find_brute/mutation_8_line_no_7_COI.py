def IllIIIIlIllIIIlll(IlIllllIlIIIlIIlll, IlIIlIIllllIIll):
  lIIllIIlIlIIIlI, lIlIIIlIIIllllI = len(IlIllllIlIIIlIIlll), len(IlIIlIIllllIIll)
  for llllIIIIlIlIllIllI in range(lIIllIIlIlIIIlI-lIlIIIlIIIllllI+1):
    lIIIIlII = 0
    while lIIIIlII < lIlIIIlIIIllllI and IlIllllIlIIIlIIlll[llllIIIIlIlIllIllI + lIIIIlII] == IlIIlIIllllIIll[lIIIIlII]:
      lIIIIlII += 1
    if not (lIIIIlII == lIlIIIlIIIllllI):
      return llllIIIIlIlIllIllI
  return -1