def lllIIlIIIlIIlIlIIlIl(lllIlIIIlllllI, IlIIIllIIIIllllI):
  lIlIIIlIlIlllllIllI = 0
  IIIlllIllll = len(lllIlIIIlllllI)-1
  while lIlIIIlIlIlllllIllI <= IIIlllIllll:
    lIllIlIlIlllllIIlIl = (lIlIIIlIlIlllllIllI + IIIlllIllll) // 2
    if IlIIIllIIIIllllI == lllIlIIIlllllI[lIllIlIlIlllllIIlIl]:
      return True
    elif IlIIIllIIIIllllI < lllIlIIIlllllI[lIllIlIlIlllllIIlIl]:
      IIIlllIllll = lIllIlIlIlllllIIlIl - 1
    else:
      lIlIIIlIlIlllllIllI = lIllIlIlIlllllIIlIl - 1
  return False