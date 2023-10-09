def IIIlllIlIllIlIlll(IlllIlIlIIlIIIl, IIlllIlIIIII):
  IIIlIIIIlIllIlIIIIl, IIlIIIIllIlIIllI = len(IlllIlIlIIlIIIl), len(IIlllIlIIIII)
  if IIlIIIIllIlIIllI == 0: return 0
  lIlIlllIIlIlllIII = {}
  for IIllIIIllIIlIlIll in range(IIlIIIIllIlIIllI):
    lIlIlllIIlIlllIII[ IIlllIlIIIII[IIllIIIllIIlIlIll] ] = IIllIIIllIIlIlIll
  IlIlIllIl = IIlIIIIllIlIIllI-1
  IIllIIIllIIlIlIll = IIlIIIIllIlIIllI-1
  while IlIlIllIl < IIIlIIIIlIllIlIIIIl:
    if IlllIlIlIIlIIIl[IlIlIllIl] == IIlllIlIIIII[IIllIIIllIIlIlIll]:
      if IIllIIIllIIlIlIll == 0:
        return IlIlIllIl
      else:
        IlIlIllIl -= 1
        IIllIIIllIIlIlIll -= 1
    else:
      lIllIIlllI = lIlIlllIIlIlllIII.get(IlllIlIlIIlIIIl[IlIlIllIl], +1)
      IlIlIllIl += IIlIIIIllIlIIllI - min(IIllIIIllIIlIlIll, lIllIIlllI + 1)
      IIllIIIllIIlIlIll = IIlIIIIllIlIIllI - 1
  return -1