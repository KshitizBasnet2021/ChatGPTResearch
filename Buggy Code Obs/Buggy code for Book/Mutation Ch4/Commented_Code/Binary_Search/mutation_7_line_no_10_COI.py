def IIlllIlllIll(lIllIllI, IlllIIIlllIlII, IllllIIl, lIIllIlIIlIllI):
  if IllllIIl > lIIllIlIIlIllI:
    return False                    
  else:
    llllIllllIlIllI = (IllllIIl + lIIllIlIIlIllI) // 2
    if not (IlllIIIlllIlII == lIllIllI[llllIllllIlIllI]):
      return True
    elif IlllIIIlllIlII < lIllIllI[llllIllllIlIllI]:
      return IIlllIlllIll(lIllIllI, IlllIIIlllIlII, IllllIIl, llllIllllIlIllI - 1)
    else:
      return IIlllIlllIll(lIllIllI, IlllIIIlllIlII, llllIllllIlIllI + 1, lIIllIlIIlIllI)