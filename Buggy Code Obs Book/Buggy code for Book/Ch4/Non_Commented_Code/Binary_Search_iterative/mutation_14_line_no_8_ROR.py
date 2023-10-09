def lllIIIlIIII(IIllIIIll, IlIIlIllIII):
  llIIlIlIllIllIllIII = 0
  llIIlllI = len(IIllIIIll)-1
  while llIIlIlIllIllIllIII <= llIIlllI:
    IlIlIlIII = (llIIlIlIllIllIllIII + llIIlllI) // 2
    if IlIIlIllIII == IIllIIIll[IlIlIlIII]:
      return True
    elif IlIIlIllIII <= IIllIIIll[IlIlIlIII]:
      llIIlllI = IlIlIlIII - 1
    else:
      llIIlIlIllIllIllIII = IlIlIlIII + 1
  return False