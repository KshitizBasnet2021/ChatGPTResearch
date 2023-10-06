def IlIIlllIlIIllI(lIIIlIll):
  for IlIlllIIlllIIIIIl in range(1, len(lIIIlIll)):
    IllIIllIlIlIl = lIIIlIll[IlIlllIIlllIIIIIl]
    IIIlIIIIIIlllIlIl = IlIlllIIlllIIIIIl
    while (IIIlIIIIIIlllIlIl > 0 and lIIIlIll[IIIlIIIIIIlllIlIl - 1] >= IllIIllIlIlIl):
      lIIIlIll[IIIlIIIIIIlllIlIl] = lIIIlIll[IIIlIIIIIIlllIlIl-1]
      IIIlIIIIIIlllIlIl -= 1
    lIIIlIll[IIIlIIIIIIlllIlIl] = IllIIllIlIlIl