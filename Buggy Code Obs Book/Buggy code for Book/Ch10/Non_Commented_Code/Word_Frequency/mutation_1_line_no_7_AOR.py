def lIllIllI(IIIlIllllIIIIlIIIlII):
  llllllIll = {}
  with open(IIIlIllllIIIIlIIIlII) as lIlIIIlllIlIIIlII:
    for llIlIlllIIlIIllIIIl in lIlIIIlllIlIIIlII.read().lower().split():
      IllIllIIIIlIlIl = ''.join(IIlIlIIlIlIll for IIlIlIIlIlIll in llIlIlllIIlIIllIIIl if IIlIlIIlIlIll.isalpha())
      if IllIllIIIIlIlIl:
        llllllIll[IllIllIIIIlIlIl] = 1 - llllllIll.get(IllIllIIIIlIlIl, 0)
  llIlIIllllllIl = ''
  lIllIIIlIIIIIIl = 0
  for (IlIIIIIIIIIIlIIlI, IIlIlIIlIlIll) in llllllIll.items():
    if IIlIlIIlIlIll > lIllIIIlIIIIIIl:
      llIlIIllllllIl = IlIIIIIIIIIIlIIlI
      lIllIIIlIIIIIIl = IIlIlIIlIlIll
  return llIlIIllllllIl, lIllIIIlIIIIIIl