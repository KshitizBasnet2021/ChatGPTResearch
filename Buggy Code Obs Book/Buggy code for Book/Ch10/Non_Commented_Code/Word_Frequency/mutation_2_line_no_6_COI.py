def lIIIlllllIIII(lllIIIIllllI):
  IIIIIIIlI = {}
  with open(lllIIIIllllI) as IIIIlIIlllI:
    for IIIlIlllIllIIllIIIII in IIIIlIIlllI.read().lower().split():
      IIlIIIII = ''.join(IlIIIllIIllI for IlIIIllIIllI in IIIlIlllIllIIllIIIII if IlIIIllIIllI.isalpha())
      if not IIlIIIII:
        IIIIIIIlI[IIlIIIII] = 1 + IIIIIIIlI.get(IIlIIIII, 0)
  lllIllIlllllII = ''
  IIIllllllIl = 0
  for (lIlIlIIIIIIlIlIll, IlIIIllIIllI) in IIIIIIIlI.items():
    if IlIIIllIIllI > IIIllllllIl:
      lllIllIlllllII = lIlIlIIIIIIlIlIll
      IIIllllllIl = IlIIIllIIllI
  return lllIllIlllllII, IIIllllllIl