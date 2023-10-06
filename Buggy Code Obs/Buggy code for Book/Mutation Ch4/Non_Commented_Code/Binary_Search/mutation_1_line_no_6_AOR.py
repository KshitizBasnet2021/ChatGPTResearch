def IIlIlllllIIllIlII(lIIlIIIll, IIIlIIlIIlI, IIIlIIIIllIllIIIIIIl, IllllIIlIllIl):
  if IIIlIIIIllIllIIIIIIl > IllllIIlIllIl:
    return False
  else:
    IIllIIlllIlII = (IIIlIIIIllIllIIIIIIl - IllllIIlIllIl) // 2
    if IIIlIIlIIlI == lIIlIIIll[IIllIIlllIlII]:
      return True
    elif IIIlIIlIIlI < lIIlIIIll[IIllIIlllIlII]:
      return IIlIlllllIIllIlII(lIIlIIIll, IIIlIIlIIlI, IIIlIIIIllIllIIIIIIl, IIllIIlllIlII - 1)
    else:
      return IIlIlllllIIllIlII(lIIlIIIll, IIIlIIlIIlI, IIllIIlllIlII + 1, IllllIIlIllIl)