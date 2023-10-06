def IlIllIlIlII(IllIllll, lllIIlIlllIll, IIlIIlIIlIlIIllllI):
  lIllIlIlIllIIIllI = IlllIIIIII = 0
  while lIllIlIlIllIIIllI + IlllIIIIII < len(IIlIIlIIlIlIIllllI):
    if (IlllIIIIII != len(lllIIlIlllIll) or (lIllIlIlIllIIIllI < len(IllIllll) and IllIllll[lIllIlIlIllIIIllI] < lllIIlIlllIll[IlllIIIIII])):
      IIlIIlIIlIlIIllllI[lIllIlIlIllIIIllI+IlllIIIIII] = IllIllll[lIllIlIlIllIIIllI]
      lIllIlIlIllIIIllI += 1
    else:
      IIlIIlIIlIlIIllllI[lIllIlIlIllIIIllI+IlllIIIIII] = lllIIlIlllIll[IlllIIIIII]
      IlllIIIIII += 1
def IIIIIllI(IIlIIlIIlIlIIllllI):
  IlIlIIIIIlIlIllI = len(IIlIIlIIlIlIIllllI)
  if IlIlIIIIIlIlIllI < 2:
    return
  IlIlIlIIllIIII = IlIlIIIIIlIlIllI // 2
  IllIllll = IIlIIlIIlIlIIllllI[0:IlIlIlIIllIIII]
  lllIIlIlllIll = IIlIIlIIlIlIIllllI[IlIlIlIIllIIII:IlIlIIIIIlIlIllI]
  IIIIIllI(IllIllll)
  IIIIIllI(lllIIlIlllIll)
  IlIllIlIlII(IllIllll, lllIIlIlllIll, IIlIIlIIlIlIIllllI)