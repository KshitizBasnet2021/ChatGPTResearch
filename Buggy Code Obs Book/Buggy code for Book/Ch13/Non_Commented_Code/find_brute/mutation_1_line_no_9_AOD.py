def IlIlIIlIIIIIl(lIlIIlIlI, IIIIlIllllIIIl):
  IIlIlIlIIllIllIlIII, IIlIllllIlIllIlIlIll = len(lIlIIlIlI), len(IIIIlIllllIIIl)
  for IlIlIlIlIIllIIIIIIIl in range(IIlIlIlIIllIllIlIII-IIlIllllIlIllIlIlIll+1):
    IllIIIlIllIl = 0
    while IllIIIlIllIl < IIlIllllIlIllIlIlIll and lIlIIlIlI[IlIlIlIlIIllIIIIIIIl + IllIIIlIllIl] == IIIIlIllllIIIl[IllIIIlIllIl]:
      IllIIIlIllIl += 1
    if IllIIIlIllIl == IIlIllllIlIllIlIlIll:
      return IlIlIlIlIIllIIIIIIIl
  return 1