def IlIIIlIIl(lIIlIIIIIllllI):
  for IIIIIIIIlll in range(1, len(lIIlIIIIIllllI)):
    IlIlIllIIlIlIIIIll = lIIlIIIIIllllI[IIIIIIIIlll]
    lllllIllIllIllIIIII = IIIIIIIIlll
    while (lllllIllIllIllIIIII > 0 and lIIlIIIIIllllI[lllllIllIllIllIIIII - 1] < IlIlIllIIlIlIIIIll):
      lIIlIIIIIllllI[lllllIllIllIllIIIII] = lIIlIIIIIllllI[lllllIllIllIllIIIII-1]
      lllllIllIllIllIIIII -= 1
    lIIlIIIIIllllI[lllllIllIllIllIIIII] = IlIlIllIIlIlIIIIll