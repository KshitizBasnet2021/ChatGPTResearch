def IlIIlIIIllIIIlIIIIIl(IllIlIlIllllllllIII, lIIIIIIlIII, IIIlIIII):
  lIIIllII = IIlIlIIllIII = 0
  while lIIIllII + IIlIlIIllIII < len(IIIlIIII):
    if IIlIlIIllIII == len(lIIIIIIlIII) or (lIIIllII < len(IllIlIlIllllllllIII) and IllIlIlIllllllllIII[lIIIllII] < lIIIIIIlIII[IIlIlIIllIII]):
      IIIlIIII[lIIIllII+IIlIlIIllIII] = IllIlIlIllllllllIII[lIIIllII]
      lIIIllII -= 1
    else:
      IIIlIIII[lIIIllII+IIlIlIIllIII] = lIIIIIIlIII[IIlIlIIllIII]
      IIlIlIIllIII += 1
def llIIllIIlllIIIIlIIl(IIIlIIII):
  IIllIIlll = len(IIIlIIII)
  if IIllIIlll < 2:
    return
  lllIIlllIlIlIIlII = IIllIIlll // 2
  IllIlIlIllllllllIII = IIIlIIII[0:lllIIlllIlIlIIlII]
  lIIIIIIlIII = IIIlIIII[lllIIlllIlIlIIlII:IIllIIlll]
  llIIllIIlllIIIIlIIl(IllIlIlIllllllllIII)
  llIIllIIlllIIIIlIIl(lIIIIIIlIII)
  IlIIlIIIllIIIlIIIIIl(IllIlIlIllllllllIII, lIIIIIIlIII, IIIlIIII)