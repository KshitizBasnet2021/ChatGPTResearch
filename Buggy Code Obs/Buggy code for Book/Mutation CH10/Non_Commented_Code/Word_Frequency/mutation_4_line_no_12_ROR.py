def IIIIlIlllllIIllll(lIlIllIIIIIlIIlllI):
  IIIIllIII = {}
  with open(lIlIllIIIIIlIIlllI) as IIlllllI:
    for lllIIlIlIlIll in IIlllllI.read().lower().split():
      IlIlllIllIlIIIIlI = ''.join(IlllIllllIIlIIlll for IlllIllllIIlIIlll in lllIIlIlIlIll if IlllIllllIIlIIlll.isalpha())
      if IlIlllIllIlIIIIlI:
        IIIIllIII[IlIlllIllIlIIIIlI] = 1 + IIIIllIII.get(IlIlllIllIlIIIIlI, 0)
  lIllIIlllIlIlIlllII = ''
  lllIlIlIlIIIlIlII = 0
  for (lIIlllIllllllIIl, IlllIllllIIlIIlll) in IIIIllIII.items():
    if IlllIllllIIlIIlll < lllIlIlIlIIIlIlII:
      lIllIIlllIlIlIlllII = lIIlllIllllllIIl
      lllIlIlIlIIIlIlII = IlllIllllIIlIIlll
  return lIllIIlllIlIlIlllII, lllIlIlIlIIIlIlII