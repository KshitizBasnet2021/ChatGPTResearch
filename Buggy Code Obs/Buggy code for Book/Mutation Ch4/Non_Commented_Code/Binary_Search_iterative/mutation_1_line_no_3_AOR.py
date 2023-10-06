def IllIlIIlllllIIllIIII(lIlIIIIIl, lIllIIIIlllII):
  IllIllIIIIIllIlllII = 0
  IIllIlIlIIlIIIIll = len(lIlIIIIIl) + 1
  while IllIllIIIIIllIlllII <= IIllIlIlIIlIIIIll:
    IIIlllllI = (IllIllIIIIIllIlllII + IIllIlIlIIlIIIIll) // 2
    if lIllIIIIlllII == lIlIIIIIl[IIIlllllI]:
      return True
    elif lIllIIIIlllII < lIlIIIIIl[IIIlllllI]:
      IIllIlIlIIlIIIIll = IIIlllllI - 1
    else:
      IllIllIIIIIllIlllII = IIIlllllI + 1
  return False