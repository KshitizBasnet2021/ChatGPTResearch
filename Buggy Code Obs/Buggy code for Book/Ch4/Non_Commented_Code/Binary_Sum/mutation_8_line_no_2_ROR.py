def lIIIIlIIIIl(lIlllIIIllIIIlllIIl, lIlIlIIIIllIIl, lIlllllllIlIllIIlIl):
  if lIlIlIIIIllIIl <= lIlllllllIlIllIIlIl:
    return 0
  elif lIlIlIIIIllIIl == lIlllllllIlIllIIlIl-1:
    return lIlllIIIllIIIlllIIl[lIlIlIIIIllIIl]
  else:
    IlIIIlIllllIIIlI = (lIlIlIIIIllIIl + lIlllllllIlIllIIlIl) // 2
    return lIIIIlIIIIl(lIlllIIIllIIIlllIIl, lIlIlIIIIllIIl, IlIIIlIllllIIIlI) + lIIIIlIIIIl(lIlllIIIllIIIlllIIl, IlIIIlIllllIIIlI, lIlllllllIlIllIIlIl)