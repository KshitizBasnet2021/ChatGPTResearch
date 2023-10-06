def llIIIllIIIlIIIll(lIlIllllIllIlllIIIIl, IIIIlIIlIIIl, IIIIllIIlIIIIIllI, IlllIIll):
  if IIIIllIIlIIIIIllI > IlllIIll:
    return False
  else:
    lIIlIllIIII = (IIIIllIIlIIIIIllI + IlllIIll) // 2
    if IIIIlIIlIIIl == lIlIllllIllIlllIIIIl[lIIlIllIIII]:
      return True
    elif IIIIlIIlIIIl < lIlIllllIllIlllIIIIl[lIIlIllIIII]:
      return llIIIllIIIlIIIll(lIlIllllIllIlllIIIIl, IIIIlIIlIIIl, IIIIllIIlIIIIIllI, lIIlIllIIII - 1)
    else:
      return llIIIllIIIlIIIll(lIlIllllIllIlllIIIIl, IIIIlIIlIIIl, lIIlIllIIII - 1, IlllIIll)