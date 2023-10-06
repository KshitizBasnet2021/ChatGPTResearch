def IIIlIlIllIl(IIllIlIIlIl, lIIlIIlllllI, llIIIllIll):
  if lIIlIIlllllI >= llIIIllIll:
    return 0
  elif lIIlIIlllllI == llIIIllIll + 1:
    return IIllIlIIlIl[lIIlIIlllllI]
  else:
    IIllIlllIIlIIIlIl = (lIIlIIlllllI + llIIIllIll) // 2
    return IIIlIlIllIl(IIllIlIIlIl, lIIlIIlllllI, IIllIlllIIlIIIlIl) + IIIlIlIllIl(IIllIlIIlIl, IIllIlllIIlIIIlIl, llIIIllIll)