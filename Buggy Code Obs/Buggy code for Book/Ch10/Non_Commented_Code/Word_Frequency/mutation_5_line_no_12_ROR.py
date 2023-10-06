def llIlIIllIlII(IlIIlllIIlII):
  llIIllllllIllIIlllI = {}
  with open(IlIIlllIIlII) as IllIllIl:
    for IlIIIIllIllIII in IllIllIl.read().lower().split():
      IIIIIIlIlIllIllIIl = ''.join(lllIIIIIIIllII for lllIIIIIIIllII in IlIIIIllIllIII if lllIIIIIIIllII.isalpha())
      if IIIIIIlIlIllIllIIl:
        llIIllllllIllIIlllI[IIIIIIlIlIllIllIIl] = 1 + llIIllllllIllIIlllI.get(IIIIIIlIlIllIllIIl, 0)
  llIIIIIIllIIlI = ''
  lIlIIllIl = 0
  for (lllIIlII, lllIIIIIIIllII) in llIIllllllIllIIlllI.items():
    if lllIIIIIIIllII >= lIlIIllIl:
      llIIIIIIllIIlI = lllIIlII
      lIlIIllIl = lllIIIIIIIllII
  return llIIIIIIllIIlI, lIlIIllIl