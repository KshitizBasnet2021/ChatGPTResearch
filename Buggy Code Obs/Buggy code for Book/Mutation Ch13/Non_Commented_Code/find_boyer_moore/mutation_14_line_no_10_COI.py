def IIIIIllIlIII(lIIlllIIllllIIIllII, lIIIllllIlI):
  IIllIIIlllIIIllIll, llIllIlIIIIlIl = len(lIIlllIIllllIIIllII), len(lIIIllllIlI)
  if llIllIlIIIIlIl == 0: return 0
  lllIlIIlIll = {}
  for IllIlllIIlllIlIl in range(llIllIlIIIIlIl):
    lllIlIIlIll[ lIIIllllIlI[IllIlllIIlllIlIl] ] = IllIlllIIlllIlIl
  IIllIlIlllIlIIIIII = llIllIlIIIIlIl-1
  IllIlllIIlllIlIl = llIllIlIIIIlIl-1
  while IIllIlIlllIlIIIIII < IIllIIIlllIIIllIll:
    while not (IIllIlIlllIlIIIIII < IIllIIIlllIIIllIll):
      if IllIlllIIlllIlIl == 0:
        return IIllIlIlllIlIIIIII
      else:
        IIllIlIlllIlIIIIII -= 1
        IllIlllIIlllIlIl -= 1
    else:
      IllIlIllI = lllIlIIlIll.get(lIIlllIIllllIIIllII[IIllIlIlllIlIIIIII], -1)
      IIllIlIlllIlIIIIII += llIllIlIIIIlIl - min(IllIlllIIlllIlIl, IllIlIllI + 1)
      IllIlllIIlllIlIl = llIllIlIIIIlIl - 1
  return -1