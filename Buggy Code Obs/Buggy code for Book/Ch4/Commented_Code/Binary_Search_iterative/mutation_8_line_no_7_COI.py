def llIllIIllIlllI(IlIlIIlllII, lIllllIIIIIlllIIl):
  IIllIIlIl = 0
  IlIlllIIlIllIIIIIll = len(IlIlIIlllII)-1
  while IIllIIlIl <= IlIlllIIlIllIIIIIll:
    IIIIlIIlllIllIlllII = (IIllIIlIl + IlIlllIIlIllIIIIIll) // 2
    if not (lIllllIIIIIlllIIl == IlIlIIlllII[IIIIlIIlllIllIlllII]):
      return True
    elif lIllllIIIIIlllIIl < IlIlIIlllII[IIIIlIIlllIllIlllII]:
      IlIlllIIlIllIIIIIll = IIIIlIIlllIllIlllII - 1                
    else:
      IIllIIlIl = IIIIlIIlllIllIlllII + 1                 
  return False                      