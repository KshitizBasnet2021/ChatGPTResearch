def IllllIlllII(IlIllIlIIllIIlIlllI, lIlIIIIllIIllllI, lIlllIIIIIIlIIllIII, lIlIIIllIIlllIIlll):
  if lIlllIIIIIIlIIllIII > lIlIIIllIIlllIIlll:
    return False
  else:
    IIlIlIIIlIIllIIllIl = (lIlllIIIIIIlIIllIII + lIlIIIllIIlllIIlll) // 2
    if lIlIIIIllIIllllI == IlIllIlIIllIIlIlllI[IIlIlIIIlIIllIIllIl]:
      return True
    elif lIlIIIIllIIllllI > IlIllIlIIllIIlIlllI[IIlIlIIIlIIllIIllIl]:
      return IllllIlllII(IlIllIlIIllIIlIlllI, lIlIIIIllIIllllI, lIlllIIIIIIlIIllIII, IIlIlIIIlIIllIIllIl - 1)
    else:
      return IllllIlllII(IlIllIlIIllIIlIlllI, lIlIIIIllIIllllI, IIlIlIIIlIIllIIllIl + 1, lIlIIIllIIlllIIlll)