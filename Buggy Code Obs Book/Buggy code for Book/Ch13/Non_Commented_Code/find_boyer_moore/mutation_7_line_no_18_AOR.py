def lllIllllllIllI(IllIllIllIll, IIllIIlIIIlIIII):
  llIlIlllllI, IIlIlIlIIIllIlIl = len(IllIllIllIll), len(IIllIIlIIIlIIII)
  if IIlIlIlIIIllIlIl == 0: return 0
  lIIIIIIIIll = {}
  for lllIIllllI in range(IIlIlIlIIIllIlIl):
    lIIIIIIIIll[ IIllIIlIIIlIIII[lllIIllllI] ] = lllIIllllI
  lllIlllIllIllI = IIlIlIlIIIllIlIl-1
  lllIIllllI = IIlIlIlIIIllIlIl-1
  while lllIlllIllIllI < llIlIlllllI:
    if IllIllIllIll[lllIlllIllIllI] == IIllIIlIIIlIIII[lllIIllllI]:
      if lllIIllllI == 0:
        return lllIlllIllIllI
      else:
        lllIlllIllIllI -= 1
        lllIIllllI -= 1
    else:
      IllIIIlIIlIllIIllI = lIIIIIIIIll.get(IllIllIllIll[lllIlllIllIllI], -1)
      lllIlllIllIllI += IIlIlIlIIIllIlIl - min(lllIIllllI, IllIIIlIIlIllIIllI - 1)
      lllIIllllI = IIlIlIlIIIllIlIl - 1
  return -1