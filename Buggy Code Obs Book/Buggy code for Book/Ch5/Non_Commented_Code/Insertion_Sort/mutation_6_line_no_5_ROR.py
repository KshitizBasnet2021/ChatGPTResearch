def IIlIlllIIlIIlIlIIlI(lllllIllIllIIIllIl):
  for lIIllIllllIIIlIIIII in range(1, len(lllllIllIllIIIllIl)):
    lllIlIIll = lllllIllIllIIIllIl[lIIllIllllIIIlIIIII]
    llIllIlllllI = lIIllIllllIIIlIIIII
    while (llIllIlllllI < 0 and lllllIllIllIIIllIl[llIllIlllllI - 1] > lllIlIIll):
      lllllIllIllIIIllIl[llIllIlllllI] = lllllIllIllIIIllIl[llIllIlllllI-1]
      llIllIlllllI -= 1
    lllllIllIllIIIllIl[llIllIlllllI] = lllIlIIll