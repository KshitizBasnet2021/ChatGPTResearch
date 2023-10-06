def IIIIlIlIIIIllIl(lIllIIlIlIll, lIIIIllIIIlIlllIllII, IIIlIIIlIIIlIllll):
  lIIlIIlIIII = IlIIIllIIIlllllIlIl = 0
  while not (lIIlIIlIIII + IlIIIllIIIlllllIlIl < len(IIIlIIIlIIIlIllll)):
    if IlIIIllIIIlllllIlIl == len(lIIIIllIIIlIlllIllII) or (lIIlIIlIIII < len(lIllIIlIlIll) and lIllIIlIlIll[lIIlIIlIIII] < lIIIIllIIIlIlllIllII[IlIIIllIIIlllllIlIl]):
      IIIlIIIlIIIlIllll[lIIlIIlIIII+IlIIIllIIIlllllIlIl] = lIllIIlIlIll[lIIlIIlIIII]
      lIIlIIlIIII += 1
    else:
      IIIlIIIlIIIlIllll[lIIlIIlIIII+IlIIIllIIIlllllIlIl] = lIIIIllIIIlIlllIllII[IlIIIllIIIlllllIlIl]
      IlIIIllIIIlllllIlIl += 1
def lIIIllIIIIIIlIllIlIl(IIIlIIIlIIIlIllll):
  IlllIlIlIllIIllI = len(IIIlIIIlIIIlIllll)
  if IlllIlIlIllIIllI < 2:
    return
  lllIIIllIllllIIlll = IlllIlIlIllIIllI // 2
  lIllIIlIlIll = IIIlIIIlIIIlIllll[0:lllIIIllIllllIIlll]
  lIIIIllIIIlIlllIllII = IIIlIIIlIIIlIllll[lllIIIllIllllIIlll:IlllIlIlIllIIllI]
  lIIIllIIIIIIlIllIlIl(lIllIIlIlIll)
  lIIIllIIIIIIlIllIlIl(lIIIIllIIIlIlllIllII)
  IIIIlIlIIIIllIl(lIllIIlIlIll, lIIIIllIIIlIlllIllII, IIIlIIIlIIIlIllll)