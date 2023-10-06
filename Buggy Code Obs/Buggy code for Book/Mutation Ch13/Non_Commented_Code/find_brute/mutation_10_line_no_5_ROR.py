def IIllIIIIIllIIIIlIlII(IIlIIIlll, IlllllllllIllIlIIlIl):
  IlIllIIIIlllllIlII, llIIlllIIIl = len(IIlIIIlll), len(IlllllllllIllIlIIlIl)
  for llIIlIllIIlIIllIII in range(IlIllIIIIlllllIlII-llIIlllIIIl+1):
    lIIllllIllIl = 0
    while (lIIllllIllIl > llIIlllIIIl and IIlIIIlll[llIIlIllIIlIIllIII + lIIllllIllIl] == IlllllllllIllIlIIlIl[lIIllllIllIl]):
      lIIllllIllIl += 1
    if lIIllllIllIl == llIIlllIIIl:
      return llIIlIllIIlIIllIII
  return -1