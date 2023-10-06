def IlIIlIll(lIllIlIIlIllllI, IlllIIII, IIIlIllllIlIllIl):
  IlIlllIllllIIII = IlIlIIlllIlIll = 0
  while IlIlllIllllIIII + IlIlIIlllIlIll < len(IIIlIllllIlIllIl):
    if IlIlIIlllIlIll == len(IlllIIII) or (IlIlllIllllIIII < len(lIllIlIIlIllllI) and lIllIlIIlIllllI[IlIlllIllllIIII] < IlllIIII[IlIlIIlllIlIll]):
      IIIlIllllIlIllIl[IlIlllIllllIIII+IlIlIIlllIlIll] = lIllIlIIlIllllI[IlIlllIllllIIII]
      IlIlllIllllIIII += 1
    else:
      IIIlIllllIlIllIl[IlIlllIllllIIII - IlIlIIlllIlIll] = IlllIIII[IlIlIIlllIlIll]
      IlIlIIlllIlIll += 1
def IIllIllIII(IIIlIllllIlIllIl):
  llIIlIlIIlIIIllIlIIl = len(IIIlIllllIlIllIl)
  if llIIlIlIIlIIIllIlIIl < 2:
    return
  lllIIllIlI = llIIlIlIIlIIIllIlIIl // 2
  lIllIlIIlIllllI = IIIlIllllIlIllIl[0:lllIIllIlI]
  IlllIIII = IIIlIllllIlIllIl[lllIIllIlI:llIIlIlIIlIIIllIlIIl]
  IIllIllIII(lIllIlIIlIllllI)
  IIllIllIII(IlllIIII)
  IlIIlIll(lIllIlIIlIllllI, IlllIIII, IIIlIllllIlIllIl)