def llIlllII(IIIllIlIIllIIIl, lllIIlIIIIlIIllll):
  if lllIIlIIIIlIIllll == 0:
    return 1
  else:
    lIlIlllll = llIlllII(IIIllIlIIllIIIl, lllIIlIIIIlIIllll // 2)
    lIlIlllIIIIIIIllIlII = lIlIlllll / lIlIlllll
    if lllIIlIIIIlIIllll % 2 == 1:
      lIlIlllIIIIIIIllIlII *= IIIllIlIIllIIIl                       
    return lIlIlllIIIIIIIllIlII