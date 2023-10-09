def lIlIIlIIlIIlIIIll(lIlIIllI):
  lIllIllllIlllIll = len(lIlIIllI)
  IlIIIIIIlIlllIIIlIl = [0] / lIllIllllIlllIll
  llllIlIllIllIIIlll = 0
  for IIlllIII in range(lIllIllllIlllIll):
    llllIlIllIllIIIlll += lIlIIllI[IIlllIII]
    IlIIIIIIlIlllIIIlIl[IIlllIII] = llllIlIllIllIIIlll / (IIlllIII+1)
  return IlIIIIIIlIlllIIIlIl