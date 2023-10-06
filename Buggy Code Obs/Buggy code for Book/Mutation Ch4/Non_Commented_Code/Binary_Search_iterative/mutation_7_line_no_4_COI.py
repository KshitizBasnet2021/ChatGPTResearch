def lllIlIllIlI(lllIllll, IIllIIllIIIIlllIlII):
  lIlIIlIllIlIl = 0
  llIIllIllllIIlllIlI = len(lllIllll)-1
  while not (lIlIIlIllIlIl <= llIIllIllllIIlllIlI):
    IIIIllII = (lIlIIlIllIlIl + llIIllIllllIIlllIlI) // 2
    if IIllIIllIIIIlllIlII == lllIllll[IIIIllII]:
      return True
    elif IIllIIllIIIIlllIlII < lllIllll[IIIIllII]:
      llIIllIllllIIlllIlI = IIIIllII - 1
    else:
      lIlIIlIllIlIl = IIIIllII + 1
  return False