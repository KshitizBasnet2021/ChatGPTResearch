def IIIIIllIllllIIlIIIlI(IllIlIllll, IIIIIIlIllIII, lllIlIlIlll, IllllIllllllllI):
  if lllIlIlIlll > IllllIllllllllI:
    return False
  else:
    IlllIIIIllIIlI = (lllIlIlIlll + IllllIllllllllI) // 2
    if IIIIIIlIllIII == IllIlIllll[IlllIIIIllIIlI]:
      return True
    elif not (IIIIIIlIllIII < IllIlIllll[IlllIIIIllIIlI]):
      return IIIIIllIllllIIlIIIlI(IllIlIllll, IIIIIIlIllIII, lllIlIlIlll, IlllIIIIllIIlI - 1)
    else:
      return IIIIIllIllllIIlIIIlI(IllIlIllll, IIIIIIlIllIII, IlllIIIIllIIlI + 1, IllllIllllllllI)