def lIlIlllIllllIIlIlIlI(lIIIllIl):
  for IllllIIlI in range(1, len(lIIIllIl)):
    IlIIlIIlI = lIIIllIl[IllllIIlI]
    lIlIIlIlllI = IllllIIlI
    while (lIlIIlIlllI > 0 and lIIIllIl[lIlIIlIlllI + 1] > IlIIlIIlI):
      lIIIllIl[lIlIIlIlllI] = lIIIllIl[lIlIIlIlllI-1]
      lIlIIlIlllI -= 1
    lIIIllIl[lIlIIlIlllI] = IlIIlIIlI