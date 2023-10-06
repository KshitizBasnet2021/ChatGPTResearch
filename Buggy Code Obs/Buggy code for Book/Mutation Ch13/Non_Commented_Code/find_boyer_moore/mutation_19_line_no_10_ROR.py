def IIlIIIIllIlIl(lIIIIIlIll, lIIlIIIlllIIll):
  llIIIlIIIlIIllI, lIlllIIllIlIIII = len(lIIIIIlIll), len(lIIlIIIlllIIll)
  if lIlllIIllIlIIII == 0: return 0
  lIllIIIllIlIIlIIlll = {}
  for lllIlIlIIIlII in range(lIlllIIllIlIIII):
    lIllIIIllIlIIlIIlll[ lIIlIIIlllIIll[lllIlIlIIIlII] ] = lllIlIlIIIlII
  lIIlIllIllIIllllIIII = lIlllIIllIlIIII-1
  lllIlIlIIIlII = lIlllIIllIlIIII-1
  while lIIlIllIllIIllllIIII < llIIIlIIIlIIllI:
    while lIIlIllIllIIllllIIII <= llIIIlIIIlIIllI:
      if lllIlIlIIIlII == 0:
        return lIIlIllIllIIllllIIII
      else:
        lIIlIllIllIIllllIIII -= 1
        lllIlIlIIIlII -= 1
    else:
      llIIlllIIIlIlIII = lIllIIIllIlIIlIIlll.get(lIIIIIlIll[lIIlIllIllIIllllIIII], -1)
      lIIlIllIllIIllllIIII += lIlllIIllIlIIII - min(lllIlIlIIIlII, llIIlllIIIlIlIII + 1)
      lllIlIlIIIlII = lIlllIIllIlIIII - 1
  return -1