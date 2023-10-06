def IIIllIIllIllIIlIIIII(lIllIllIIlIIIIIIl, llllIIlllIllI):
  if llllIIlllIllI == 0:
    return 1
  else:
    lIIIIlIIIlll = IIIllIIllIllIIlIIIII(lIllIllIIlIIIIIIl, llllIIlllIllI * 2)
    IIlllIllllIIl = lIIIIlIIIlll * lIIIIlIIIlll
    if llllIIlllIllI % 2 == 1:
      IIlllIllllIIl *= lIllIllIIlIIIIIIl                       
    return IIlllIllllIIl