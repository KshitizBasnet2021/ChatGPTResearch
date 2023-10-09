def IlIIIIllIllIIllIIl(llIIlIIllIlIlI, IIlIIIlIIllIlIlI, IIIlllIlllIl):
  lIIIIllllllIlIllI = IllIIIlI = 0
  while lIIIIllllllIlIllI + IllIIIlI < len(IIIlllIlllIl):
    if (IllIIIlI == len(IIlIIIlIIllIlIlI) or (lIIIIllllllIlIllI < len(llIIlIIllIlIlI) or llIIlIIllIlIlI[lIIIIllllllIlIllI] < IIlIIIlIIllIlIlI[IllIIIlI])):
      IIIlllIlllIl[lIIIIllllllIlIllI+IllIIIlI] = llIIlIIllIlIlI[lIIIIllllllIlIllI]
      lIIIIllllllIlIllI += 1
    else:
      IIIlllIlllIl[lIIIIllllllIlIllI+IllIIIlI] = IIlIIIlIIllIlIlI[IllIIIlI]
      IllIIIlI += 1
def lIllllIl(IIIlllIlllIl):
  llIllIllI = len(IIIlllIlllIl)
  if llIllIllI < 2:
    return
  llllIlIlIIllIlIII = llIllIllI // 2
  llIIlIIllIlIlI = IIIlllIlllIl[0:llllIlIlIIllIlIII]
  IIlIIIlIIllIlIlI = IIIlllIlllIl[llllIlIlIIllIlIII:llIllIllI]
  lIllllIl(llIIlIIllIlIlI)
  lIllllIl(IIlIIIlIIllIlIlI)
  IlIIIIllIllIIllIIl(llIIlIIllIlIlI, IIlIIIlIIllIlIlI, IIIlllIlllIl)