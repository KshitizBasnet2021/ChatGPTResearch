def lIlIIIll(lIlIllIIlIlIIlI, IIllIllIll, llIlllIllI, IIIIlllIlI):
  if llIlllIllI > IIIIlllIlI:
    return False
  else:
    lIllIIIlIllI = (llIlllIllI + IIIIlllIlI) // 2
    if IIllIllIll == lIlIllIIlIlIIlI[lIllIIIlIllI]:
      return True
    elif IIllIllIll <= lIlIllIIlIlIIlI[lIllIIIlIllI]:
      return lIlIIIll(lIlIllIIlIlIIlI, IIllIllIll, llIlllIllI, lIllIIIlIllI - 1)
    else:
      return lIlIIIll(lIlIllIIlIlIIlI, IIllIllIll, lIllIIIlIllI + 1, IIIIlllIlI)