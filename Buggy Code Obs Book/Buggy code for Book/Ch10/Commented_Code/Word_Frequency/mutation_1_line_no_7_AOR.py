def llIIllIlIIIIlIllIl(llIIllIlIIllI):
  IlIllIIII = {}
  with open(llIIllIlIIllI) as lllIllIl:
    for IIIIIIlIlllIIlII in lllIllIl.read().lower().split():
      llIlIlIllIlIIlllI = ''.join(IIIlIllllIlI for IIIlIllllIlI in IIIIIIlIlllIIlII if IIIlIllllIlI.isalpha())
      if llIlIlIllIlIIlllI:
        IlIllIIII[llIlIlIllIlIIlllI] = 1 - IlIllIIII.get(llIlIlIllIlIIlllI, 0)
  IIllIIlI = ''
  IIlIIllIlIIlIIIlIIII = 0
  for (llIIllllIIlllIIllllI, IIIlIllllIlI) in IlIllIIII.items():
    if IIIlIllllIlI > IIlIIllIlIIlIIIlIIII:
      IIllIIlI = llIIllllIIlllIIllllI
      IIlIIllIlIIlIIIlIIII = IIIlIllllIlI
  return IIllIIlI, IIlIIllIlIIlIIIlIIII