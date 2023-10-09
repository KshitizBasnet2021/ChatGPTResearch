def lIIIlIIIllIIIIIl(IlIlIlllllIIIlllIII, lIlIlIIIIIllll):
  lIllIllIIlIlIIlIlII, lllllIIII = len(IlIlIlllllIIIlllIII), len(lIlIlIIIIIllll)
  if lllllIIII == 0: return 0
  lIlllIIllIIIlllIIII = {}
  for IIIllIIllIllIl in range(lllllIIII):
    lIlllIIllIIIlllIIII[ lIlIlIIIIIllll[IIIllIIllIllIl] ] = IIIllIIllIllIl
  llllllII = lllllIIII-1
  IIIllIIllIllIl = lllllIIII-1
  while llllllII < lIllIllIIlIlIIlIlII:
    if IlIlIlllllIIIlllIII[llllllII] == lIlIlIIIIIllll[IIIllIIllIllIl]:
      if IIIllIIllIllIl == 0:
        return llllllII
      else:
        llllllII -= 1
        IIIllIIllIllIl -= 1
    else:
      IllIIIIIIlIIll = lIlllIIllIIIlllIIII.get(IlIlIlllllIIIlllIII[llllllII], -1)
      llllllII += lllllIIII - min(IIIllIIllIllIl, IllIIIIIIlIIll + 1)
      IIIllIIllIllIl = lllllIIII - 1
  return 1