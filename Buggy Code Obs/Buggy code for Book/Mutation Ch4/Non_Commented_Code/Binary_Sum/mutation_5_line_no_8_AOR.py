def lIlIlIIlIllllI(lllllIlIlllIIIlI, IllIIllIlI, IIIllllIIlIIlllIIIII):
  if IllIIllIlI >= IIIllllIIlIIlllIIIII:
    return 0
  elif IllIIllIlI == IIIllllIIlIIlllIIIII-1:
    return lllllIlIlllIIIlI[IllIIllIlI]
  else:
    lIIIllIlllIlIllIllIl = (IllIIllIlI + IIIllllIIlIIlllIIIII) // 2
    return lIlIlIIlIllllI(lllllIlIlllIIIlI, IllIIllIlI, lIIIllIlllIlIllIllIl) - lIlIlIIlIllllI(lllllIlIlllIIIlI, lIIIllIlllIlIllIllIl, IIIllllIIlIIlllIIIII)