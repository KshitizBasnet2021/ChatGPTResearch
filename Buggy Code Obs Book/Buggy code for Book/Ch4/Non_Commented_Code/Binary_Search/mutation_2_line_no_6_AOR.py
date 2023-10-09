def IlllIIIIIIIIllI(lllllIIIlIllI, IlIIllll, IIIlIIllllIIIII, IlIIlIlllllIIIIIIIlI):
  if IIIlIIllllIIIII > IlIIlIlllllIIIIIIIlI:
    return False
  else:
    IllIllIllIIIl = (IIIlIIllllIIIII + IlIIlIlllllIIIIIIIlI) / 2
    if IlIIllll == lllllIIIlIllI[IllIllIllIIIl]:
      return True
    elif IlIIllll < lllllIIIlIllI[IllIllIllIIIl]:
      return IlllIIIIIIIIllI(lllllIIIlIllI, IlIIllll, IIIlIIllllIIIII, IllIllIllIIIl - 1)
    else:
      return IlllIIIIIIIIllI(lllllIIIlIllI, IlIIllll, IllIllIllIIIl + 1, IlIIlIlllllIIIIIIIlI)