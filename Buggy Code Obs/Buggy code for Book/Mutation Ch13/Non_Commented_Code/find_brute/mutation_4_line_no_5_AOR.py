def IIIlllIIIII(IIIIlIlll, IIIIIIIIlllI):
  lIlIIllIllI, IIIlIllIIlI = len(IIIIlIlll), len(IIIIIIIIlllI)
  for llIlllIIlIlIlI in range(lIlIIllIllI-IIIlIllIIlI+1):
    llllIIIllIIl = 0
    while (llllIIIllIIl < IIIlIllIIlI and IIIIlIlll[llIlllIIlIlIlI - llllIIIllIIl] == IIIIIIIIlllI[llllIIIllIIl]):
      llllIIIllIIl += 1
    if llllIIIllIIl == IIIlIllIIlI:
      return llIlllIIlIlIlI
  return -1