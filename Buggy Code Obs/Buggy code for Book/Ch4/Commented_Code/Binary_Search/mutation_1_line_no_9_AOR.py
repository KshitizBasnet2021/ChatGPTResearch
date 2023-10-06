def IlIlIIllIlIllII(IIlIIIllIlll, IIIIIIlllIlIlIII, IlIllIIlIlIl, IllllllIlllIllI):
  if IlIllIIlIlIl > IllllllIlllIllI:
    return False                    
  else:
    lllIlllIIlIlI = (IlIllIIlIlIl - IllllllIlllIllI) // 2
    if IIIIIIlllIlIlIII == IIlIIIllIlll[lllIlllIIlIlI]:         
      return True
    elif IIIIIIlllIlIlIII < IIlIIIllIlll[lllIlllIIlIlI]:
      return IlIlIIllIlIllII(IIlIIIllIlll, IIIIIIlllIlIlIII, IlIllIIlIlIl, lllIlllIIlIlI - 1)
    else:
      return IlIlIIllIlIllII(IIlIIIllIlll, IIIIIIlllIlIlIII, lllIlllIIlIlI + 1, IllllllIlllIllI)