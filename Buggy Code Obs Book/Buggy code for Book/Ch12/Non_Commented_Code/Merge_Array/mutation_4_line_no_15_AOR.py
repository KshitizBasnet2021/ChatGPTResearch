def IlIIIIIlIIlI(IIIIIlIIlII, IIIIlIIlIIlIIIlll, lllIIlIIIlIIIl):
  IIlIIIIlII = lIIIlIIllIII = 0
  while IIlIIIIlII + lIIIlIIllIII < len(lllIIlIIIlIIIl):
    if lIIIlIIllIII == len(IIIIlIIlIIlIIIlll) or (IIlIIIIlII < len(IIIIIlIIlII) and IIIIIlIIlII[IIlIIIIlII] < IIIIlIIlIIlIIIlll[lIIIlIIllIII]):
      lllIIlIIIlIIIl[IIlIIIIlII+lIIIlIIllIII] = IIIIIlIIlII[IIlIIIIlII]
      IIlIIIIlII += 1
    else:
      lllIIlIIIlIIIl[IIlIIIIlII+lIIIlIIllIII] = IIIIlIIlIIlIIIlll[lIIIlIIllIII]
      lIIIlIIllIII += 1
def lIIIllIIIIIllIlIIl(lllIIlIIIlIIIl):
  llIlIllIIllI = len(lllIIlIIIlIIIl)
  if llIlIllIIllI < 2:
    return
  lIllIIlIIl = llIlIllIIllI / 2
  IIIIIlIIlII = lllIIlIIIlIIIl[0:lIllIIlIIl]
  IIIIlIIlIIlIIIlll = lllIIlIIIlIIIl[lIllIIlIIl:llIlIllIIllI]
  lIIIllIIIIIllIlIIl(IIIIIlIIlII)
  lIIIllIIIIIllIlIIl(IIIIlIIlIIlIIIlll)
  IlIIIIIlIIlI(IIIIIlIIlII, IIIIlIIlIIlIIIlll, lllIIlIIIlIIIl)