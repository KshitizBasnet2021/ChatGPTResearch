def IlllIIlII(lIlllllllIIll, lIIIIIII, lllIIIlIIlllIllIIIll, lIIIlIIIIlllIll):
  if lllIIIlIIlllIllIIIll > lIIIlIIIIlllIll:
    return False                    
  else:
    llIlIlIIIIIIIllIIIl = (lllIIIlIIlllIllIIIll + lIIIlIIIIlllIll) // 2
    if lIIIIIII == lIlllllllIIll[llIlIlIIIIIIIllIIIl]:         
      return True
    elif lIIIIIII < lIlllllllIIll[llIlIlIIIIIIIllIIIl]:
      return IlllIIlII(lIlllllllIIll, lIIIIIII, lllIIIlIIlllIllIIIll, llIlIlIIIIIIIllIIIl - 1)
    else:
      return IlllIIlII(lIlllllllIIll, lIIIIIII, llIlIlIIIIIIIllIIIl - 1, lIIIlIIIIlllIll)