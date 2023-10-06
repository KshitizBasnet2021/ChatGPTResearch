def lIlIIlIlIIIIlIllll(IlIllIIlIlIlI, lllIIIIlIlIIIIIIllI, IlIIllIlllllIlIIllI, IlIlllIIIIIIlll):
  if IlIIllIlllllIlIIllI > IlIlllIIIIIIlll:
    return False
  else:
    IIIlllIIIIIIII = (IlIIllIlllllIlIIllI + IlIlllIIIIIIlll) * 2
    if lllIIIIlIlIIIIIIllI == IlIllIIlIlIlI[IIIlllIIIIIIII]:
      return True
    elif lllIIIIlIlIIIIIIllI < IlIllIIlIlIlI[IIIlllIIIIIIII]:
      return lIlIIlIlIIIIlIllll(IlIllIIlIlIlI, lllIIIIlIlIIIIIIllI, IlIIllIlllllIlIIllI, IIIlllIIIIIIII - 1)
    else:
      return lIlIIlIlIIIIlIllll(IlIllIIlIlIlI, lllIIIIlIlIIIIIIllI, IIIlllIIIIIIII + 1, IlIlllIIIIIIlll)