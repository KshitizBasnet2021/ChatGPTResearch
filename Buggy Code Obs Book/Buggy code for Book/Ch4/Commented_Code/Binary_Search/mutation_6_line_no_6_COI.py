def lIllIlll(lllIIlIlIIIIlllIlll, llIIlIIIllIllIIIl, IllIIIIIlIllIIIIIIII, llIIIlIIllIlIlIIIIll):
  if not (IllIIIIIlIllIIIIIIII > llIIIlIIllIlIlIIIIll):
    return False                    
  else:
    IlIlIIIIIIII = (IllIIIIIlIllIIIIIIII + llIIIlIIllIlIlIIIIll) // 2
    if llIIlIIIllIllIIIl == lllIIlIlIIIIlllIlll[IlIlIIIIIIII]:         
      return True
    elif llIIlIIIllIllIIIl < lllIIlIlIIIIlllIlll[IlIlIIIIIIII]:
      return lIllIlll(lllIIlIlIIIIlllIlll, llIIlIIIllIllIIIl, IllIIIIIlIllIIIIIIII, IlIlIIIIIIII - 1)
    else:
      return lIllIlll(lllIIlIlIIIIlllIlll, llIIlIIIllIllIIIl, IlIlIIIIIIII + 1, llIIIlIIllIlIlIIIIll)