def llIIIlllllII(lIlIllIllIIIl, IIIllIlIll, llIlIIlllllll):
  if IIIllIlIll >= llIlIIlllllll:
    return 0
  elif IIIllIlIll == llIlIIlllllll-1:
    return lIlIllIllIIIl[IIIllIlIll]
  else:
    IIlIIIIllIllllIIIIIl = (IIIllIlIll + llIlIIlllllll) / 2
    return llIIIlllllII(lIlIllIllIIIl, IIIllIlIll, IIlIIIIllIllllIIIIIl) + llIIIlllllII(lIlIllIllIIIl, IIlIIIIllIllllIIIIIl, llIlIIlllllll)