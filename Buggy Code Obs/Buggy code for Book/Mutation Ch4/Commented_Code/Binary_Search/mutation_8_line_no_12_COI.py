def llIIlIIIIllIII(lllllllIlIlllIllllll, lIlllllllIIlll, llIllIllIlllll, IIlIIIIllIIll):
  if llIllIllIlllll > IIlIIIIllIIll:
    return False                    
  else:
    lllllIllIlIllIIIIIl = (llIllIllIlllll + IIlIIIIllIIll) // 2
    if lIlllllllIIlll == lllllllIlIlllIllllll[lllllIllIlIllIIIIIl]:         
      return True
    elif not (lIlllllllIIlll < lllllllIlIlllIllllll[lllllIllIlIllIIIIIl]):
      return llIIlIIIIllIII(lllllllIlIlllIllllll, lIlllllllIIlll, llIllIllIlllll, lllllIllIlIllIIIIIl - 1)
    else:
      return llIIlIIIIllIII(lllllllIlIlllIllllll, lIlllllllIIlll, lllllIllIlIllIIIIIl + 1, IIlIIIIllIIll)