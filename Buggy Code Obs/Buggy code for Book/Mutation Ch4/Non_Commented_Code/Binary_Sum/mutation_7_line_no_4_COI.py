def IIIIIIIlllIIIll(IlIIlIlIlIIIllIlIII, llllIllIlIIllI, IIIlIIlIl):
  if llllIllIlIIllI >= IIIlIIlIl:
    return 0
  elif not (llllIllIlIIllI == IIIlIIlIl - 1):
    return IlIIlIlIlIIIllIlIII[llllIllIlIIllI]
  else:
    IIIIIlIIIIlIIl = (llllIllIlIIllI + IIIlIIlIl) // 2
    return IIIIIIIlllIIIll(IlIIlIlIlIIIllIlIII, llllIllIlIIllI, IIIIIlIIIIlIIl) + IIIIIIIlllIIIll(IlIIlIlIlIIIllIlIII, IIIIIlIIIIlIIl, IIIlIIlIl)