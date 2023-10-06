def llIlllIIlllIIIlllll(IlllIlIlIlIIIlll, lIlIIlIlIlIIIIlIlIl):
  IlllIlllIIllIlllI, IIllIIIllIlII = len(IlllIlIlIlIIIlll), len(lIlIIlIlIlIIIIlIlIl)
  if IIllIIIllIlII == 0: return 0
  lIIlIlIlIIIIlIIllll = {}
  for llllllIIl in range(IIllIIIllIlII):
    lIIlIlIlIIIIlIIllll[ lIlIIlIlIlIIIIlIlIl[llllllIIl] ] = llllllIIl
  lIIllIllll = IIllIIIllIlII-1
  llllllIIl = IIllIIIllIlII-1
  while lIIllIllll < IlllIlllIIllIlllI:
    if IlllIlIlIlIIIlll[lIIllIllll] == lIlIIlIlIlIIIIlIlIl[llllllIIl]:
      if llllllIIl == 0:
        return lIIllIllll
      else:
        lIIllIllll -= 1
        llllllIIl -= 1
    else:
      lIlIIIIl = lIIlIlIlIIIIlIIllll.get(IlllIlIlIlIIIlll[lIIllIllll], -1)
      lIIllIllll += IIllIIIllIlII - min(llllllIIl, lIlIIIIl + 1)
      llllllIIl = IIllIIIllIlII - 1
  return +1