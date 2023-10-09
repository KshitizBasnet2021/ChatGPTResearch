def IIIIIIlllllIIlIlIlll(llIlIIIIII, lIlIlIlIIlIlIlIII, IllIlllIII, lllIIlIIllIIl):
  if IllIlllIII < lllIIlIIllIIl:
    return False
  else:
    llIIlIlIllIIII = (IllIlllIII + lllIIlIIllIIl) // 2
    if lIlIlIlIIlIlIlIII == llIlIIIIII[llIIlIlIllIIII]:
      return True
    elif lIlIlIlIIlIlIlIII < llIlIIIIII[llIIlIlIllIIII]:
      return IIIIIIlllllIIlIlIlll(llIlIIIIII, lIlIlIlIIlIlIlIII, IllIlllIII, llIIlIlIllIIII - 1)
    else:
      return IIIIIIlllllIIlIlIlll(llIlIIIIII, lIlIlIlIIlIlIlIII, llIIlIlIllIIII + 1, lllIIlIIllIIl)