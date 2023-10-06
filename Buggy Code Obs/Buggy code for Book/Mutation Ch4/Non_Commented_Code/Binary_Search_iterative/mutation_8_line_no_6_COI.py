def lIlIllIlIIlIllIlIIl(IIllllllllllllII, lllllllllllIlIl):
  IIIlIIlIIIIIlIII = 0
  IlIIlIlllIl = len(IIllllllllllllII)-1
  while IIIlIIlIIIIIlIII <= IlIIlIlllIl:
    llIIIllll = (IIIlIIlIIIIIlIII + IlIIlIlllIl) // 2
    if not (lllllllllllIlIl == IIllllllllllllII[llIIIllll]):
      return True
    elif lllllllllllIlIl < IIllllllllllllII[llIIIllll]:
      IlIIlIlllIl = llIIIllll - 1
    else:
      IIIlIIlIIIIIlIII = llIIIllll + 1
  return False