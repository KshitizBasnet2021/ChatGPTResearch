def lllIlIIIl(lIlIIIllIIlllIl, lllIlIlIllIlIlllIIII, IIIIIlIIIlIlll):
  lllllIllllllIlI = llIIIIIlllllIll = 0
  while lllllIllllllIlI + llIIIIIlllllIll < len(IIIIIlIIIlIlll):
    if llIIIIIlllllIll == len(lllIlIlIllIlIlllIIII) or (lllllIllllllIlI < len(lIlIIIllIIlllIl) and lIlIIIllIIlllIl[lllllIllllllIlI] < lllIlIlIllIlIlllIIII[llIIIIIlllllIll]):
      IIIIIlIIIlIlll[lllllIllllllIlI - llIIIIIlllllIll] = lIlIIIllIIlllIl[lllllIllllllIlI]
      lllllIllllllIlI += 1
    else:
      IIIIIlIIIlIlll[lllllIllllllIlI+llIIIIIlllllIll] = lllIlIlIllIlIlllIIII[llIIIIIlllllIll]
      llIIIIIlllllIll += 1
def lIIlIIIllIIlIllllllI(IIIIIlIIIlIlll):
  IllIlIIIIlIIl = len(IIIIIlIIIlIlll)
  if IllIlIIIIlIIl < 2:
    return
  llIIlIllllIIlIlII = IllIlIIIIlIIl // 2
  lIlIIIllIIlllIl = IIIIIlIIIlIlll[0:llIIlIllllIIlIlII]
  lllIlIlIllIlIlllIIII = IIIIIlIIIlIlll[llIIlIllllIIlIlII:IllIlIIIIlIIl]
  lIIlIIIllIIlIllllllI(lIlIIIllIIlllIl)
  lIIlIIIllIIlIllllllI(lllIlIlIllIlIlllIIII)
  lllIlIIIl(lIlIIIllIIlllIl, lllIlIlIllIlIlllIIII, IIIIIlIIIlIlll)