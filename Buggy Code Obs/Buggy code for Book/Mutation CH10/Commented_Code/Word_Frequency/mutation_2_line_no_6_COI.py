def IIIllIIIlIl(IlIlIlll):
  lIIIllIlI = {}
  with open(IlIlIlll) as llIIIllIIlIII:
    for IllIIIIIIllIlIIllI in llIIIllIIlIII.read().lower().split():
      lIllIlIIlIllIII = ''.join(lIIIIlIllllllllllIl for lIIIIlIllllllllllIl in IllIIIIIIllIlIIllI if lIIIIlIllllllllllIl.isalpha())
      if not lIllIlIIlIllIII:
        lIIIllIlI[lIllIlIIlIllIII] = 1 + lIIIllIlI.get(lIllIlIIlIllIII, 0)
  llIIlIlIllllIlIIIll = ''
  IllIIlIllIlllllll = 0
  for (lIIllIlllllIllIIl, lIIIIlIllllllllllIl) in lIIIllIlI.items():
    if lIIIIlIllllllllllIl > IllIIlIllIlllllll:
      llIIlIlIllllIlIIIll = lIIllIlllllIllIIl
      IllIIlIllIlllllll = lIIIIlIllllllllllIl
  return llIIlIlIllllIlIIIll, IllIIlIllIlllllll