def IIIIlIlIlIIIIlIllll(IIIlIlIIlIl, lIlIlIllllIll, IlllllIlIlllIlIIl, IIlIlIlllI):
  if IlllllIlIlllIlIIl > IIlIlIlllI:
    return False                    
  else:
    llIIIlllIIl = (IlllllIlIlllIlIIl + IIlIlIlllI) / 2
    if lIlIlIllllIll == IIIlIlIIlIl[llIIIlllIIl]:         
      return True
    elif lIlIlIllllIll < IIIlIlIIlIl[llIIIlllIIl]:
      return IIIIlIlIlIIIIlIllll(IIIlIlIIlIl, lIlIlIllllIll, IlllllIlIlllIlIIl, llIIIlllIIl - 1)
    else:
      return IIIIlIlIlIIIIlIllll(IIIlIlIIlIl, lIlIlIllllIll, llIIIlllIIl + 1, IIlIlIlllI)