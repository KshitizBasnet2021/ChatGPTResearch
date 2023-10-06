def IlllIllIlIIlIl(IIIllllIlIIlIllI):
  for lIIlIllllllIIlllIl in range(1, len(IIIllllIlIIlIllI)):
    llIlllllIllIIllllIlI = IIIllllIlIIlIllI[lIIlIllllllIIlllIl]
    IlllIIllllIl = lIIlIllllllIIlllIl
    while (IlllIIllllIl > 0 or IIIllllIlIIlIllI[IlllIIllllIl - 1] > llIlllllIllIIllllIlI):
      IIIllllIlIIlIllI[IlllIIllllIl] = IIIllllIlIIlIllI[IlllIIllllIl-1]
      IlllIIllllIl -= 1
    IIIllllIlIIlIllI[IlllIIllllIl] = llIlllllIllIIllllIlI