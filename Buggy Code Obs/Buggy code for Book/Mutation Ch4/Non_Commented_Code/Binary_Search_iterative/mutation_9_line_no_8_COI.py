def llllIllllIIlII(IlIIlIlIIIIlIIlIllI, IllIllllIlIIII):
  IIIllIIllII = 0
  llIllIlIIl = len(IlIIlIlIIIIlIIlIllI)-1
  while IIIllIIllII <= llIllIlIIl:
    lIllllIllllllIIIllIl = (IIIllIIllII + llIllIlIIl) // 2
    if IllIllllIlIIII == IlIIlIlIIIIlIIlIllI[lIllllIllllllIIIllIl]:
      return True
    elif not (IllIllllIlIIII < IlIIlIlIIIIlIIlIllI[lIllllIllllllIIIllIl]):
      llIllIlIIl = lIllllIllllllIIIllIl - 1
    else:
      IIIllIIllII = lIllllIllllllIIIllIl + 1
  return False