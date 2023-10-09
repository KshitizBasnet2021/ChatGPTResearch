def llIlIIIIIIlIllII(lIIIlIllll, llIIlIIIll):
  IIllllIlllIIlIIIIllI = 0
  IIIIIIlIIIIIlI = len(lIIIlIllll)-1
  while IIllllIlllIIlIIIIllI <= IIIIIIlIIIIIlI:
    lIlIllllllIlIII = (IIllllIlllIIlIIIIllI + IIIIIIlIIIIIlI) // 2
    if llIIlIIIll == lIIIlIllll[lIlIllllllIlIII]:
      return True
    elif llIIlIIIll < lIIIlIllll[lIlIllllllIlIII]:
      IIIIIIlIIIIIlI = lIlIllllllIlIII + 1
    else:
      IIllllIlllIIlIIIIllI = lIlIllllllIlIII + 1
  return False