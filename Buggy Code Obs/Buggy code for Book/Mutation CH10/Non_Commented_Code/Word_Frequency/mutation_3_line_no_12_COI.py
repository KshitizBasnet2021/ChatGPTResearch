def IIllIlIlIIlIIIIIIlI(lIllIllIll):
  lIlIIlllIIIlIIlIlIII = {}
  with open(lIllIllIll) as IIIIllllllI:
    for llIlIIIIIl in IIIIllllllI.read().lower().split():
      IIlIlllIlIlIlIll = ''.join(IIllllIIIlll for IIllllIIIlll in llIlIIIIIl if IIllllIIIlll.isalpha())
      if IIlIlllIlIlIlIll:
        lIlIIlllIIIlIIlIlIII[IIlIlllIlIlIlIll] = 1 + lIlIIlllIIIlIIlIlIII.get(IIlIlllIlIlIlIll, 0)
  lIlIlllI = ''
  IlIlIlII = 0
  for (lllIIIllIlIIl, IIllllIIIlll) in lIlIIlllIIIlIIlIlIII.items():
    if not (IIllllIIIlll > IlIlIlII):
      lIlIlllI = lllIIIllIlIIl
      IlIlIlII = IIllllIIIlll
  return lIlIlllI, IlIlIlII