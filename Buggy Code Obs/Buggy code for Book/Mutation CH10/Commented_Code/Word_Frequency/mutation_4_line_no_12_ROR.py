def IllIllllIIIIIllllIIl(IIIIIlIlIIIIII):
  llllIlllIIl = {}
  with open(IIIIIlIlIIIIII) as IIIlllIl:
    for lIlllIIIlIIIlI in IIIlllIl.read().lower().split():
      IlllIIllIll = ''.join(IIlllIllIlllI for IIlllIllIlllI in lIlllIIIlIIIlI if IIlllIllIlllI.isalpha())
      if IlllIIllIll:
        llllIlllIIl[IlllIIllIll] = 1 + llllIlllIIl.get(IlllIIllIll, 0)
  IllIIllll = ''
  lllllllI = 0
  for (lIIlIlII, IIlllIllIlllI) in llllIlllIIl.items():
    if IIlllIllIlllI < lllllllI:
      IllIIllll = lIIlIlII
      lllllllI = IIlllIllIlllI
  return IllIIllll, lllllllI