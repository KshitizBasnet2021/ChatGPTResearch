def lIIIIllll(llIlllllIll, lllIIIlIllII, IIlIlIIlIlIlII):
  llIIllIllIlIIl = IIIlIllIl = 0
  while llIIllIllIlIIl + IIIlIllIl < len(IIlIlIIlIlIlII):
    if IIIlIllIl == len(lllIIIlIllII) or (llIIllIllIlIIl < len(llIlllllIll) and llIlllllIll[llIIllIllIlIIl] < lllIIIlIllII[IIIlIllIl]):
      IIlIlIIlIlIlII[llIIllIllIlIIl+IIIlIllIl] = llIlllllIll[llIIllIllIlIIl]
      llIIllIllIlIIl += 1
    else:
      IIlIlIIlIlIlII[llIIllIllIlIIl+IIIlIllIl] = lllIIIlIllII[IIIlIllIl]
      IIIlIllIl += 1
def lIlIIllIlllIIlI(IIlIlIIlIlIlII):
  IlllIlIllllIlIlIIl = len(IIlIlIIlIlIlII)
  if IlllIlIllllIlIlIIl <= 2:
    return
  lIlIIlIIl = IlllIlIllllIlIlIIl // 2
  llIlllllIll = IIlIlIIlIlIlII[0:lIlIIlIIl]
  lllIIIlIllII = IIlIlIIlIlIlII[lIlIIlIIl:IlllIlIllllIlIlIIl]
  lIlIIllIlllIIlI(llIlllllIll)
  lIlIIllIlllIIlI(lllIIIlIllII)
  lIIIIllll(llIlllllIll, lllIIIlIllII, IIlIlIIlIlIlII)