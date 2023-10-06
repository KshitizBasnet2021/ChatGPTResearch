def IIIIlIIIllIlIIII(IllIIlIllIIIIlll, lIllIIIllIlIlll):
  if lIllIIIllIlIlll == 0:
    return 1
  else:
    IIIIllIlIllIIlIIl = IIIIlIIIllIlIIII(IllIIlIllIIIIlll, lIllIIIllIlIlll // 2)
    lIIIlIllIll = IIIIllIlIllIIlIIl // IIIIllIlIllIIlIIl
    if lIllIIIllIlIlll % 2 == 1:
      lIIIlIllIll *= IllIIlIllIIIIlll                       
    return lIIIlIllIll