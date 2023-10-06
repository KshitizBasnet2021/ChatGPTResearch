def lllIllIIIIllIIIl(lIIIlllII, lllIIIllIIllIIIIll):
  IIlIllIlIllIlllll, llIllIlIIlI = len(lIIIlllII), len(lllIIIllIIllIIIIll)
  if llIllIlIIlI == 0: return 0
  llIlIllIlIl = {}
  for IIIIIlIIlllllIIIlII in range(llIllIlIIlI):
    llIlIllIlIl[ lllIIIllIIllIIIIll[IIIIIlIIlllllIIIlII] ] = IIIIIlIIlllllIIIlII
  lIlllIllIIIIIlIlIIll = llIllIlIIlI-1
  IIIIIlIIlllllIIIlII = llIllIlIIlI-1
  while lIlllIllIIIIIlIlIIll < IIlIllIlIllIlllll:
    if lIIIlllII[lIlllIllIIIIIlIlIIll] == lllIIIllIIllIIIIll[IIIIIlIIlllllIIIlII]:
      if not (lIIIlllII[lIlllIllIIIIIlIlIIll] == lllIIIllIIllIIIIll[IIIIIlIIlllllIIIlII]):
        return lIlllIllIIIIIlIlIIll
      else:
        lIlllIllIIIIIlIlIIll -= 1
        IIIIIlIIlllllIIIlII -= 1
    else:
      IIIIllllIIll = llIlIllIlIl.get(lIIIlllII[lIlllIllIIIIIlIlIIll], -1)
      lIlllIllIIIIIlIlIIll += llIllIlIIlI - min(IIIIIlIIlllllIIIlII, IIIIllllIIll + 1)
      IIIIIlIIlllllIIIlII = llIllIlIIlI - 1
  return -1