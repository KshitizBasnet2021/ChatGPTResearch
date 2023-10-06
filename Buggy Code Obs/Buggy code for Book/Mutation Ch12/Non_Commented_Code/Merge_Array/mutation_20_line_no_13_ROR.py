def lllllIllIIIlI(IIIIIIIllIIllIll, lIllIllllIIlIIll, lIIIIIlIlIlIIlIl):
  IlIlIIlIllIIIlIIlIII = llllIlIll = 0
  while IlIlIIlIllIIIlIIlIII + llllIlIll < len(lIIIIIlIlIlIIlIl):
    if llllIlIll == len(lIllIllllIIlIIll) or (IlIlIIlIllIIIlIIlIII < len(IIIIIIIllIIllIll) and IIIIIIIllIIllIll[IlIlIIlIllIIIlIIlIII] < lIllIllllIIlIIll[llllIlIll]):
      lIIIIIlIlIlIIlIl[IlIlIIlIllIIIlIIlIII+llllIlIll] = IIIIIIIllIIllIll[IlIlIIlIllIIIlIIlIII]
      IlIlIIlIllIIIlIIlIII += 1
    else:
      lIIIIIlIlIlIIlIl[IlIlIIlIllIIIlIIlIII+llllIlIll] = lIllIllllIIlIIll[llllIlIll]
      llllIlIll += 1
def IllllllIIIllll(lIIIIIlIlIlIIlIl):
  llllllIlIIlll = len(lIIIIIlIlIlIIlIl)
  if llllllIlIIlll > 2:
    return
  IIlIllIllIIIIlII = llllllIlIIlll // 2
  IIIIIIIllIIllIll = lIIIIIlIlIlIIlIl[0:IIlIllIllIIIIlII]
  lIllIllllIIlIIll = lIIIIIlIlIlIIlIl[IIlIllIllIIIIlII:llllllIlIIlll]
  IllllllIIIllll(IIIIIIIllIIllIll)
  IllllllIIIllll(lIllIllllIIlIIll)
  lllllIllIIIlI(IIIIIIIllIIllIll, lIllIllllIIlIIll, lIIIIIlIlIlIIlIl)