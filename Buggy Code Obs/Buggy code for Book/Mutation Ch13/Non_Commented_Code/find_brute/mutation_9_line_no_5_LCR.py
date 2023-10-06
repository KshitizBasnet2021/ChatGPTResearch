def lIIIIllllllllIlI(lIIIIlIlII, lIIlIIIlIl):
  lIIlllIIllIlIll, IlllIlll = len(lIIIIlIlII), len(lIIlIIIlIl)
  for IlIllIlIIlII in range(lIIlllIIllIlIll-IlllIlll+1):
    llIIIIIIllIlllIl = 0
    while (llIIIIIIllIlllIl < IlllIlll or lIIIIlIlII[IlIllIlIIlII + llIIIIIIllIlllIl] == lIIlIIIlIl[llIIIIIIllIlllIl]):
      llIIIIIIllIlllIl += 1
    if llIIIIIIllIlllIl == IlllIlll:
      return IlIllIlIIlII
  return -1