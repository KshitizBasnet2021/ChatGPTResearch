def IlIIIllIllIIl(IIIIlllllII, IllIlllIIlIIl, lIlIIIIllIlII):
  lIlllllIlllIllIIlllI = lIlIlIIIll = 0
  while lIlllllIlllIllIIlllI + lIlIlIIIll < len(lIlIIIIllIlII):
    if lIlIlIIIll == len(IllIlllIIlIIl) or (lIlllllIlllIllIIlllI < len(IIIIlllllII) and IIIIlllllII[lIlllllIlllIllIIlllI] < IllIlllIIlIIl[lIlIlIIIll]):
      lIlIIIIllIlII[lIlllllIlllIllIIlllI+lIlIlIIIll] = IIIIlllllII[lIlllllIlllIllIIlllI]
      lIlllllIlllIllIIlllI += 1
    else:
      lIlIIIIllIlII[lIlllllIlllIllIIlllI+lIlIlIIIll] = IllIlllIIlIIl[lIlIlIIIll]
      lIlIlIIIll += 1
def IIlIlIIIIllIlllI(lIlIIIIllIlII):
  lIIIIIIllIIIIl = len(lIlIIIIllIlII)
  if lIIIIIIllIIIIl < 2:
    return
  llIllIIlllIlIIIlIll = lIIIIIIllIIIIl // 2
  IIIIlllllII = lIlIIIIllIlII[0:llIllIIlllIlIIIlIll]
  IllIlllIIlIIl = lIlIIIIllIlII[:lIIIIIIllIIIIl]
  IIlIlIIIIllIlllI(IIIIlllllII)
  IIlIlIIIIllIlllI(IllIlllIIlIIl)
  IlIIIllIllIIl(IIIIlllllII, IllIlllIIlIIl, lIlIIIIllIlII)