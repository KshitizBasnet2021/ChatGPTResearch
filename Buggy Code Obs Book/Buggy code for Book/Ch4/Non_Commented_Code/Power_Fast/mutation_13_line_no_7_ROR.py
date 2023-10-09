def IIIlIlIllIl(lllIlIIlllI, IIlIlllIIIllIlllIlll):
  if IIlIlllIIIllIlllIlll == 0:
    return 1
  else:
    lllIIlllIIIllIll = IIIlIlIllIl(lllIlIIlllI, IIlIlllIIIllIlllIlll // 2)
    IlIllIlIIIIIIllIII = lllIIlllIIIllIll * lllIIlllIIIllIll
    if IIlIlllIIIllIlllIlll % 2 != 1:
      IlIllIlIIIIIIllIII *= lllIlIIlllI                       
    return IlIllIlIIIIIIllIII