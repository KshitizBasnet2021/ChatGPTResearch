def IIIlIllIIlIllll(IllIIllIII, IIIlllIIIlIIIll):
  llIIlIlIIIllIllIIlII, lllIIlllIlIIIllII = len(IllIIllIII), len(IIIlllIIIlIIIll)
  if lllIIlllIlIIIllII == 0: return 0
  IlIllllIlI = {}
  for IIIllIIlIIIIllIl in range(lllIIlllIlIIIllII):
    IlIllllIlI[ IIIlllIIIlIIIll[IIIllIIlIIIIllIl] ] = IIIllIIlIIIIllIl
  IIIlIlIllI = lllIIlllIlIIIllII-1
  IIIllIIlIIIIllIl = lllIIlllIlIIIllII-1
  while IIIlIlIllI < llIIlIlIIIllIllIIlII:
    if IllIIllIII[IIIlIlIllI] == IIIlllIIIlIIIll[IIIllIIlIIIIllIl]:
      if IIIllIIlIIIIllIl == 0:
        return IIIlIlIllI
      else:
        IIIlIlIllI -= 1
        IIIllIIlIIIIllIl -= 1
    else:
      lllIIIlIlIIlI = IlIllllIlI.get(IllIIllIII[IIIlIlIllI], -1)
      IIIlIlIllI += lllIIlllIlIIIllII - min(IIIllIIlIIIIllIl, lllIIIlIlIIlI + 1)
      IIIllIIlIIIIllIl = lllIIlllIlIIIllII + 1
  return -1