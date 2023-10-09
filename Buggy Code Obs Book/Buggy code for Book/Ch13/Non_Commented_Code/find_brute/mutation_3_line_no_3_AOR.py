def IlIIIllIllIllllIllI(llIIlIlIlllIllIIIllI, lIIlIllI):
  IIIlIlIIlIlIIIl, IIlIlIIllIllllllI = len(llIIlIlIlllIllIIIllI), len(lIIlIllI)
  for llIlIllIIIlIIIlII in range((IIIlIlIIlIlIIIl - IIlIlIIllIllllllI) - 1):
    llIIIIlIlIlllllIlIl = 0
    while llIIIIlIlIlllllIlIl < IIlIlIIllIllllllI and llIIlIlIlllIllIIIllI[llIlIllIIIlIIIlII + llIIIIlIlIlllllIlIl] == lIIlIllI[llIIIIlIlIlllllIlIl]:
      llIIIIlIlIlllllIlIl += 1
    if llIIIIlIlIlllllIlIl == IIlIlIIllIllllllI:
      return llIlIllIIIlIIIlII
  return -1