def llIllllIIIl(IllIIlIIIIIIIllI, IlllllII):
  lIIlIllllIl, IIIlIlllIIllIIIlI = len(IllIIlIIIIIIIllI), len(IlllllII)
  for llIlIllIIllIll in range(lIIlIllllIl-IIIlIlllIIllIIIlI+1):
    lIIlIllIlIlllI = 0
    while lIIlIllIlIlllI < IIIlIlllIIllIIIlI and IllIIlIIIIIIIllI[llIlIllIIllIll + lIIlIllIlIlllI] == IlllllII[lIIlIllIlIlllI]:
      lIIlIllIlIlllI += 1
    if lIIlIllIlIlllI != IIIlIlllIIllIIIlI:
      return llIlIllIIllIll
  return -1