def IIIllIIll(IlIIllIllIIIIIII, IIIIllllIlIlllIIIIIl):
  IlIlIIIllIIlIIIlllI, llIlllIIII = len(IlIIllIllIIIIIII), len(IIIIllllIlIlllIIIIIl)
  if llIlllIIII == 0: return 0
  IIIlIIllIIlIlIII = {}
  for llIIIlIIlIIlII in range(llIlllIIII):
    IIIlIIllIIlIlIII[ IIIIllllIlIlllIIIIIl[llIIIlIIlIIlII] ] = llIIIlIIlIIlII
  IIIIIIlI = llIlllIIII-1
  llIIIlIIlIIlII = llIlllIIII-1
  while IIIIIIlI < IlIlIIIllIIlIIIlllI:
    if IlIIllIllIIIIIII[IIIIIIlI] == IIIIllllIlIlllIIIIIl[llIIIlIIlIIlII]:
      if IlIIllIllIIIIIII[IIIIIIlI] != IIIIllllIlIlllIIIIIl[llIIIlIIlIIlII]:
        return IIIIIIlI
      else:
        IIIIIIlI -= 1
        llIIIlIIlIIlII -= 1
    else:
      lIIlIIIIIlIII = IIIlIIllIIlIlIII.get(IlIIllIllIIIIIII[IIIIIIlI], -1)
      IIIIIIlI += llIlllIIII - min(llIIIlIIlIIlII, lIIlIIIIIlIII + 1)
      llIIIlIIlIIlII = llIlllIIII - 1
  return -1