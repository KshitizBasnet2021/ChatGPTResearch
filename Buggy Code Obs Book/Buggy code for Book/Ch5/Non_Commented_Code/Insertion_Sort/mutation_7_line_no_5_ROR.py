def IIlIIllII(IlIlIIlIlllIlIlllII):
  for lIIIlIlllI in range(1, len(IlIlIIlIlllIlIlllII)):
    IlIlIlIllIIllllIIIIl = IlIlIIlIlllIlIlllII[lIIIlIlllI]
    lIlIllllIIllI = lIIIlIlllI
    while (lIlIllllIIllI >= 0 and IlIlIIlIlllIlIlllII[lIlIllllIIllI - 1] > IlIlIlIllIIllllIIIIl):
      IlIlIIlIlllIlIlllII[lIlIllllIIllI] = IlIlIIlIlllIlIlllII[lIlIllllIIllI-1]
      lIlIllllIIllI -= 1
    IlIlIIlIlllIlIlllII[lIlIllllIIllI] = IlIlIlIllIIllllIIIIl