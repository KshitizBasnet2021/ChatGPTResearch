def IllIIllllIl(llIllllllIIlIIllIllI, IlllIllIlllIlIIIll, IlIlIIlIll, IIIIlIlIlIl):
  if not (IlIlIIlIll > IIIIlIlIlIl):
    return False
  else:
    lIIIllllllllIIII = (IlIlIIlIll + IIIIlIlIlIl) // 2
    if IlllIllIlllIlIIIll == llIllllllIIlIIllIllI[lIIIllllllllIIII]:
      return True
    elif IlllIllIlllIlIIIll < llIllllllIIlIIllIllI[lIIIllllllllIIII]:
      return IllIIllllIl(llIllllllIIlIIllIllI, IlllIllIlllIlIIIll, IlIlIIlIll, lIIIllllllllIIII - 1)
    else:
      return IllIIllllIl(llIllllllIIlIIllIllI, IlllIllIlllIlIIIll, lIIIllllllllIIII + 1, IIIIlIlIlIl)