def lIlIlIIlIIIlIlIIl(llIlIIIlllll):
  IIllIIIIl = len(llIlIIIlllll)
  IlIllIIll = [0] * IIllIIIIl
  lIIlIIIlIIll = 0
  for IllllIIIIIlIIlIII in range(IIllIIIIl):
    lIIlIIIlIIll += llIlIIIlllll[IllllIIIIIlIIlIII]
    IlIllIIll[IllllIIIIIlIIlIII] = lIIlIIIlIIll // (IllllIIIIIlIIlIII + 1)
  return IlIllIIll