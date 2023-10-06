def lIIIllIIIIllIlIIl(IlIIIlIIlll, llIlIIllI, lllIlllI, llIlIllIl):
  if lllIlllI > llIlIllIl:
    return False
  else:
    IIllIlIII = (lllIlllI + llIlIllIl) // 2
    if llIlIIllI == IlIIIlIIlll[IIllIlIII]:
      return True
    elif llIlIIllI < IlIIIlIIlll[IIllIlIII]:
      return lIIIllIIIIllIlIIl(IlIIIlIIlll, llIlIIllI, lllIlllI, IIllIlIII + 1)
    else:
      return lIIIllIIIIllIlIIl(IlIIIlIIlll, llIlIIllI, IIllIlIII + 1, llIlIllIl)