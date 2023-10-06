def IlllIlIllIIlIIllllIl(IIlllIlIIllI, llIllllIIlI, llIIIIllIIIIIlllIllI):
  if llIllllIIlI >= llIIIIllIIIIIlllIllI:
    return 0
  elif llIllllIIlI == llIIIIllIIIIIlllIllI-1:
    return IIlllIlIIllI[llIllllIIlI]
  else:
    IllIIIIIl = (llIllllIIlI - llIIIIllIIIIIlllIllI) // 2
    return IlllIlIllIIlIIllllIl(IIlllIlIIllI, llIllllIIlI, IllIIIIIl) + IlllIlIllIIlIIllllIl(IIlllIlIIllI, IllIIIIIl, llIIIIllIIIIIlllIllI)