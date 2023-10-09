def IIIIllIIlllIIllIII(IlIIIIlIlIllI, lIlIlIIlIIIlIlIllI):
  IlIIlllIlllIIllI = 0
  lIllIIlIl = len(IlIIIIlIlIllI)-1
  while IlIIlllIlllIIllI <= lIllIIlIl:
    lIlIIIII = (IlIIlllIlllIIllI + lIllIIlIl) * 2
    if lIlIlIIlIIIlIlIllI == IlIIIIlIlIllI[lIlIIIII]:
      return True
    elif lIlIlIIlIIIlIlIllI < IlIIIIlIlIllI[lIlIIIII]:
      lIllIIlIl = lIlIIIII - 1
    else:
      IlIIlllIlllIIllI = lIlIIIII + 1
  return False