def llIlIIIIlIllllIl(IlIllIlIIllIIIIIlll, IlIIIIIlIl):
  IlIIlllIIIIIl = 0
  IIllIIllIIllIIII = len(IlIllIlIIllIIIIIlll)-1
  while IlIIlllIIIIIl <= IIllIIllIIllIIII:
    IIlIIlIIIIIIlIIlll = (IlIIlllIIIIIl + IIllIIllIIllIIII) // 2
    if IlIIIIIlIl == IlIllIlIIllIIIIIlll[IIlIIlIIIIIIlIIlll]:
      return True
    elif IlIIIIIlIl > IlIllIlIIllIIIIIlll[IIlIIlIIIIIIlIIlll]:
      IIllIIllIIllIIII = IIlIIlIIIIIIlIIlll - 1
    else:
      IlIIlllIIIIIl = IIlIIlIIIIIIlIIlll + 1
  return False