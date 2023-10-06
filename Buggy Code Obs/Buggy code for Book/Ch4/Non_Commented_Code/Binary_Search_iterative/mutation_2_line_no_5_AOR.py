def llIlIIIlllIlll(IlllIlIIIIII, lIlIIIIIlIlIllIlIl):
  IllllIlIl = 0
  IlIIllIIIIIl = len(IlllIlIIIIII)-1
  while IllllIlIl <= IlIIllIIIIIl:
    lIlIllIIIlIl = (IllllIlIl - IlIIllIIIIIl) // 2
    if lIlIIIIIlIlIllIlIl == IlllIlIIIIII[lIlIllIIIlIl]:
      return True
    elif lIlIIIIIlIlIllIlIl < IlllIlIIIIII[lIlIllIIIlIl]:
      IlIIllIIIIIl = lIlIllIIIlIl - 1
    else:
      IllllIlIl = lIlIllIIIlIl + 1
  return False