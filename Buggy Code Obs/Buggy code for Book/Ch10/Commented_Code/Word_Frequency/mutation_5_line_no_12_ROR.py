def lIlIlIllllIllIIlIlll(IllIlIIllIIllIlIIl):
  llllIlIIIIIlII = {}
  with open(IllIlIIllIIllIlIIl) as lIIIIIllIIlllll:
    for lIlIIlIIIIIlI in lIIIIIllIIlllll.read().lower().split():
      llIIlIlIlI = ''.join(IIIlIlllIlllI for IIIlIlllIlllI in lIlIIlIIIIIlI if IIIlIlllIlllI.isalpha())
      if llIIlIlIlI:
        llllIlIIIIIlII[llIIlIlIlI] = 1 + llllIlIIIIIlII.get(llIIlIlIlI, 0)
  llIllIllllIIlIIlll = ''
  IllIllIIIll = 0
  for (lIlllIII, IIIlIlllIlllI) in llllIlIIIIIlII.items():
    if IIIlIlllIlllI >= IllIllIIIll:
      llIllIllllIIlIIlll = lIlllIII
      IllIllIIIll = IIIlIlllIlllI
  return llIllIllllIIlIIlll, IllIllIIIll