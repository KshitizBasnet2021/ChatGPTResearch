def IIlIllIIllIlllIIIl(lIlIIlllIIlIllII, IlIIIlII, lIllIllIIIIIlIIlllII):
  lIIIllIlIIIIIlIlI = lllllIlII = 0
  while lIIIllIlIIIIIlIlI + lllllIlII > len(lIllIllIIIIIlIIlllII):
    if lllllIlII == len(IlIIIlII) or (lIIIllIlIIIIIlIlI < len(lIlIIlllIIlIllII) and lIlIIlllIIlIllII[lIIIllIlIIIIIlIlI] < IlIIIlII[lllllIlII]):
      lIllIllIIIIIlIIlllII[lIIIllIlIIIIIlIlI+lllllIlII] = lIlIIlllIIlIllII[lIIIllIlIIIIIlIlI]
      lIIIllIlIIIIIlIlI += 1
    else:
      lIllIllIIIIIlIIlllII[lIIIllIlIIIIIlIlI+lllllIlII] = IlIIIlII[lllllIlII]
      lllllIlII += 1
def lIllIlIl(lIllIllIIIIIlIIlllII):
  lIIllllIIll = len(lIllIllIIIIIlIIlllII)
  if lIIllllIIll < 2:
    return
  IlIIIlIIIII = lIIllllIIll // 2
  lIlIIlllIIlIllII = lIllIllIIIIIlIIlllII[0:IlIIIlIIIII]
  IlIIIlII = lIllIllIIIIIlIIlllII[IlIIIlIIIII:lIIllllIIll]
  lIllIlIl(lIlIIlllIIlIllII)
  lIllIlIl(IlIIIlII)
  IIlIllIIllIlllIIIl(lIlIIlllIIlIllII, IlIIIlII, lIllIllIIIIIlIIlllII)