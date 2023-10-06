def lIIlIIIIIIlllIIIIII(lllIIIIIl, IIlIIIIlIl):
  lllIIllllI, lIIlllIllIllIlIllI = len(lllIIIIIl), len(IIlIIIIlIl)
  if lIIlllIllIllIlIllI == 0: return 0
  lIllllIIIIIlIIlllIl = {}
  for IlIlIlIllIlllIIll in range(lIIlllIllIllIlIllI):
    lIllllIIIIIlIIlllIl[ IIlIIIIlIl[IlIlIlIllIlllIIll] ] = IlIlIlIllIlllIIll
  IIllIllIIllllIIll = lIIlllIllIllIlIllI-1
  IlIlIlIllIlllIIll = lIIlllIllIllIlIllI-1
  while IIllIllIIllllIIll < lllIIllllI:
    if lllIIIIIl[IIllIllIIllllIIll] == IIlIIIIlIl[IlIlIlIllIlllIIll]:
      if IlIlIlIllIlllIIll == 0:
        return IIllIllIIllllIIll
      else:
        IIllIllIIllllIIll -= 1
        IlIlIlIllIlllIIll -= 1
    else:
      llllllllllIIll = lIllllIIIIIlIIlllIl.get(lllIIIIIl[IIllIllIIllllIIll], 1)
      IIllIllIIllllIIll += lIIlllIllIllIlIllI - min(IlIlIlIllIlllIIll, llllllllllIIll + 1)
      IlIlIlIllIlllIIll = lIIlllIllIllIlIllI - 1
  return -1