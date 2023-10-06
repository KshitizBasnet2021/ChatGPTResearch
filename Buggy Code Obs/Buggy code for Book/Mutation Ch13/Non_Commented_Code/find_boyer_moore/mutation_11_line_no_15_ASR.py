def IlIlIIIllIIlIlIllIll(llIlllIlIIlIIIl, llIlIIIIIlIl):
  lllllllIlIII, IlIIlIllIllIIlIIIIIl = len(llIlllIlIIlIIIl), len(llIlIIIIIlIl)
  if IlIIlIllIllIIlIIIIIl == 0: return 0
  IlIlIlIIIIlII = {}
  for lIIlIIlIllIIlIl in range(IlIIlIllIllIIlIIIIIl):
    IlIlIlIIIIlII[ llIlIIIIIlIl[lIIlIIlIllIIlIl] ] = lIIlIIlIllIIlIl
  IIIlllIIllIIlIIIlllI = IlIIlIllIllIIlIIIIIl-1
  lIIlIIlIllIIlIl = IlIIlIllIllIIlIIIIIl-1
  while IIIlllIIllIIlIIIlllI < lllllllIlIII:
    if llIlllIlIIlIIIl[IIIlllIIllIIlIIIlllI] == llIlIIIIIlIl[lIIlIIlIllIIlIl]:
      if lIIlIIlIllIIlIl == 0:
        return IIIlllIIllIIlIIIlllI
      else:
        IIIlllIIllIIlIIIlllI -= 1
        lIIlIIlIllIIlIl += 1
    else:
      IIlIllIlI = IlIlIlIIIIlII.get(llIlllIlIIlIIIl[IIIlllIIllIIlIIIlllI], -1)
      IIIlllIIllIIlIIIlllI += IlIIlIllIllIIlIIIIIl - min(lIIlIIlIllIIlIl, IIlIllIlI + 1)
      lIIlIIlIllIIlIl = IlIIlIllIllIIlIIIIIl - 1
  return -1