def lIIllIII(IIlIlllIllllI, IIIlIIIlllIIIIIIIl):
  lllIlllI = 0
  llIIlIlIlllIIllll = len(IIlIlllIllllI)-1
  while lllIlllI < llIIlIlIlllIIllll:
    lIIlIIlllIIlllI = (lllIlllI + llIIlIlIlllIIllll) // 2
    if IIIlIIIlllIIIIIIIl == IIlIlllIllllI[lIIlIIlllIIlllI]:
      return True
    elif IIIlIIIlllIIIIIIIl < IIlIlllIllllI[lIIlIIlllIIlllI]:
      llIIlIlIlllIIllll = lIIlIIlllIIlllI - 1
    else:
      lllIlllI = lIIlIIlllIIlllI + 1
  return False