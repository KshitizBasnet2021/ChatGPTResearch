def IIIIlIIlIlIlIlI(lllllIllIl, llllIlllIll, IIllIIIlIIII, lIIllllI):
  if IIllIIIlIIII > lIIllllI:
    return False                    
  else:
    IIlllIIllllIllIll = (IIllIIIlIIII + lIIllllI) // 2
    if llllIlllIll == lllllIllIl[IIlllIIllllIllIll]:         
      return True
    elif llllIlllIll > lllllIllIl[IIlllIIllllIllIll]:
      return IIIIlIIlIlIlIlI(lllllIllIl, llllIlllIll, IIllIIIlIIII, IIlllIIllllIllIll - 1)
    else:
      return IIIIlIIlIlIlIlI(lllllIllIl, llllIlllIll, IIlllIIllllIllIll + 1, lIIllllI)