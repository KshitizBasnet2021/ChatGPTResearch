def IlIlIlIIlllIlIll(lIIIlIlIlIIIIIIl):
  for lIIIllIlIlI in range(1, len(lIIIlIlIlIIIIIIl)):
    IlIIllIIIll = lIIIlIlIlIIIIIIl[lIIIllIlIlI]
    lllllIllllIlIllIII = lIIIllIlIlI
    while lllllIllllIlIllIII > 0 and lIIIlIlIlIIIIIIl[lllllIllllIlIllIII-1] > IlIIllIIIll:
      lIIIlIlIlIIIIIIl[lllllIllllIlIllIII] = lIIIlIlIlIIIIIIl[lllllIllllIlIllIII + 1]
      lllllIllllIlIllIII -= 1
    lIIIlIlIlIIIIIIl[lllllIllllIlIllIII] = IlIIllIIIll