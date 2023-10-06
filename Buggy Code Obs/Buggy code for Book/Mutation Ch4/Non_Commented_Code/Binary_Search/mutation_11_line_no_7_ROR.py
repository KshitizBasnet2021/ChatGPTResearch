def llIlIlllIlIllIIIII(llIlllIIlIllIl, IIlIIIlllIl, lIllllllIlIllIlII, llllllllllIlIIlIllI):
  if lIllllllIlIllIlII > llllllllllIlIIlIllI:
    return False
  else:
    IIIIlIlllIIIllIIllI = (lIllllllIlIllIlII + llllllllllIlIIlIllI) // 2
    if IIlIIIlllIl != llIlllIIlIllIl[IIIIlIlllIIIllIIllI]:
      return True
    elif IIlIIIlllIl < llIlllIIlIllIl[IIIIlIlllIIIllIIllI]:
      return llIlIlllIlIllIIIII(llIlllIIlIllIl, IIlIIIlllIl, lIllllllIlIllIlII, IIIIlIlllIIIllIIllI - 1)
    else:
      return llIlIlllIlIllIIIII(llIlllIIlIllIl, IIlIIIlllIl, IIIIlIlllIIIllIIllI + 1, llllllllllIlIIlIllI)